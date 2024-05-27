<template>
  <div class="container" @dragover.prevent @drop="handleDrop">
    <div v-if="!loading">
      <input type="file" style="display: none" ref="fileInput" @change="handleFileChange">
      <button id="btn" @click="$refs.fileInput.click()">Escolher Arquivo</button>
    </div>
    <div v-else class="loading-message">
      Carregando...
    </div>
  </div>
  <div id="response" v-if="loadProgress">
    <span>POS:  <progress class="progress" :value="sentiments['POS']*100" max="100"></progress> </span>
    
    <span>NEG:  <progress class="progress" :value="sentiments['NEG']*100" max="100"></progress> </span>
    <span>NEU:  <progress class="progress" :value="sentiments['NEU']*100" max="100"></progress> </span>
  </div>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';

export default {
  setup() {
    const loading = ref(false);
    const loadProgress = ref(false);
    const sentiments = ref(null)
    const handleFileChange = (event) => {
      const file = event.target.files[0];
      analyzeSentiment(file);
    };

    const handleDrop = (event) => {
      event.preventDefault();
      const file = event.dataTransfer.files[0];
      analyzeSentiment(file);
    };

    const analyzeSentiment = async (file) => {
      loading.value = true;
      const formData = new FormData();
      formData.append('file', file);
      try {
        const response = await axios.post('http://127.0.0.1:5000//analyze', formData);
        sentiments.value = response.data["Porcentagens de cada sentimento:"];
        console.log(sentiments.value['POS']);
        loadProgress.value = false ? false: true;
        // Faça o que quiser com as porcentagens de sentimento aqui
      } catch (error) {
        console.error('Erro ao analisar sentimento:', error);
      } finally {
        loading.value = false;
      }
    };

    return {
      loading,
      handleFileChange,
      handleDrop,
      loadProgress,
      sentiments
    };
  }
};
</script>

<style>
    .container {
      width: 400px;
      height: 500px;
      display: flex;
      justify-content: center;
      align-items: center;
      border: 2px dashed #ccc;
    }

    #btn {
      padding: 10px 20px;
      font-size: 16px;
      background-color: #4CAF50;
      color: white;
      border: none;
      cursor: pointer;
      border-radius: 5px;
      transition: background-color 0.3s;
    }

    #btn:hover {
      background-color: #45a049;
    }

    .loading-message {
      font-size: 18px;
    }

    #response{ 
      width: 400px;
      height: 500px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      justify-content: center;
      align-items: center;
      border: 2px dashed #ccc;
    }




    .progress {
      width: 100%;
      height: 20px;
      appearance: none;
      -webkit-appearance: none;
      border: none;
      border-radius: 10px;
      background-color: #ddd;
    }

    .progress::-webkit-progress-bar {
      background-color: #ddd;
      border-radius: 10px;
    }

    .progress::-webkit-progress-value {
      background-color: #4CAF50;
      border-radius: 10px;
    }
  </style>

<template>
    <div class="home">
      <MovieList />
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  import MovieList from '@/components/MovieList.vue'; // @ is an alias to /src
  
  export default defineComponent({
    name: 'HomeView',
    components: {
      MovieList,
    },
  });
  </script>
  
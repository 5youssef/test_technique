<template>


  <v-card class="mx-auto" max-width="344">
    <v-img
      src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
      height="200px"
      cover
    ></v-img>

    <v-card-title>
      {{ movie.title }}
    </v-card-title>

    <v-card-subtitle>
      {{ movie.description }}
    </v-card-subtitle>

    <!-- Add a button to get movie details -->
    <v-btn color="primary" @click="getMovieDetails(movie.id)">Get Details</v-btn>
  </v-card>
</template>

<script>
import { useRouter } from 'vue-router';

export default {
  props: ['movie'],
  setup(props) {
    const router = useRouter();

    const getMovieDetails = (id) => {
      router.push({ name: 'show-movie', params: { id: id } });
    };

    return {
      getMovieDetails,
    };
  },
};
</script>

<style scoped>
/* Add any custom styles here */
</style>



<template>
    <div>
        <v-row>
            <v-col cols="12">
                <nav aria-label="breadcrumb">
                    <slot></slot>
                </nav>
                <h1 class="yellow--text">List of movies</h1>
            </v-col>
            
        </v-row>
        <v-row>

            <v-col cols="12" class="text-right mt-3">
                <v-btn @click="displayForm" :color="showForm ? 'primary' : 'secondary'" small>
                    {{ showForm ? 'Close' : 'New' }}
                </v-btn>
            </v-col>
        </v-row>
        
        <v-row>
            <v-col v-for="movie in movies" :key="movie.id" cols="12" md="4">
                <OneMovie :movie="movie" @delete="deleteOneMovie" />
            </v-col>
        </v-row>
        
        <teleport to="#alert" v-if="movieDeleted">
            <v-alert color="error" class="text-center">
                <strong>movie is deleted!</strong>
            </v-alert>
        </teleport>
        
        <teleport to="#alert" v-if="movieAdded">
            <v-alert color="success" class="text-center">
                <strong>movie is added successfully!</strong>
            </v-alert>
        </teleport>
    </div>
</template>



<script>
import { ref, onMounted } from 'vue';
import OneMovie from './OneMovie.vue';
import axios from 'axios';

export default {
    components: {
        OneMovie,
    },
    setup() {
        const movieDeleted = ref(false);
        const movieAdded = ref(false);
        const showForm = ref(false);
        const movies = ref([]);
        
        const getData = async () => {
            try {
                const response = await axios.get('http://localhost:8000/api/movies/');
                movies.value = response.data;
            } catch (error) {
                console.log(error);
            }
        };
        
        const deleteOneMovie = (id) => {
            movies.value = movies.value.filter((movie) => movie.id !== id);
            movieDeleted.value = true;
            setTimeout(() => {
                movieDeleted.value = false;
            }, 3000);
        };
        
        const addMovie = (movie) => {
            movies.value.push(movie);
            showForm.value = false;
            movieAdded.value = true;
            setTimeout(() => {
                movieAdded.value = false;
            }, 3000);
        };
        
        const displayForm = () => {
            showForm.value = !showForm.value;
        };
        
        onMounted(() => {
            getData();
        });
        
        return {
            movieDeleted,
            movieAdded,
            showForm,
            movies,
            deleteOneMovie,
            addMovie,
            displayForm,
        };
    },
};
</script>

<style scoped>
h1.yellow--text {
    color: #ffc107;
    text-align: center;
}
</style>

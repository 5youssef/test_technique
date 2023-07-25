

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
            <v-col v-for="movie in movies" :key="movie.id" cols="12" md="4">
                <OneMovie :movie="movie" />
            </v-col>
        </v-row>
        <v-row>
            <v-pagination v-model="currentPage" :total-visible="5" :length="totalPages"   @input="getData"   />
        </v-row>
        
        
    </div>
</template>



<script>
import { ref, onMounted, watch } from 'vue';
import OneMovie from './OneMovie.vue';
import axios from 'axios';
import { useRouter } from 'vue-router'


export default {
    components: {
        OneMovie,
    },
    setup() {
        const movies = ref([]);
        const paginatedData = ref([]);
        const currentPage = ref();
        const perPage = 5;
        const totalPages = ref();
        
        
        const router = useRouter();
        
        
        const getData = async () => {
            try {
                const response = await axios.get(`http://localhost:8000/api/movies/?page=${currentPage.value}`);
                movies.value = response.data;
                totalPages.value = movies.value.total_pages
                movies.value =  movies.value.data;
            } catch (error) {
                console.log(error);
            }
        };
        const getMovieDetails = (id) => {
            console.log(id);
            router.push(`/movie/${id}`);
        };
        
        
        
        onMounted(() => {
            getData();
        });
        
        watch(currentPage, () => {
            getData();
        });
        
        return {
            movies,
            paginatedData,
            currentPage,
            perPage,
            totalPages,
            getData,
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

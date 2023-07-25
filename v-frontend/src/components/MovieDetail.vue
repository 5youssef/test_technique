<template>
    <div class="row" v-if="showForm">
        <div class="col-md-6 mx-auto">
            <EditMovie :movie="movie" @add="editMovie($event)"/>
        </div>
    </div>   
    <v-row>
        <v-col class="mx-auto" cols="8" md="6">
            <nav aria-label="breadcrumb">
                <slot></slot>
            </nav>
            <h1 class="text-h5">Show Movie</h1>
        </v-col>
        
        <!-- New button -->
        <v-col class="mx-auto" cols="8" md="6" >
            <v-btn
            @click="displayForm"
            :color="showForm ? 'primary' : 'success'"
            >
            {{ showForm ? 'Close' : 'Edit' }}
        </v-btn>
    </v-col>
</v-row>
<v-row>
    <v-col cols="12">
        <div v-if="movie">
            <v-card class="mx-auto" max-width="500">
                <v-img
                src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
                height="200px"
                cover
                ></v-img>
                
                <v-card-title>
                    {{ movie.movie.title }}
                </v-card-title>
                
                <v-card-subtitle>
                    {{ movie.movie.description }}
                </v-card-subtitle>
                
                <!-- Reviews -->
                <div v-if="movie.reviews.length > 0">
                    <h4>Reviews {{  movie.average_grade }} </h4>
                    <div>
                        <h2>Rate this item:</h2>
                        <div class="text-center">
                            <v-rating
                            v-model="rating"
                            bg-color="orange-lighten-1"
                            color="blue"
                            ></v-rating>
                            <v-btn color="primary" @click="postRating">Submit Rating</v-btn>
                            
                        </div>    
                    </div>
                </div>
                
                <div v-else>
                    <p>No reviews yet.</p>
                </div>
            </v-card>
            
        </div>
        <div v-else>
            Loading...
        </div>
        
    </v-col>
    
</v-row>

</template>

<script>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import { useStore } from 'vuex';
import EditMovie from './EditMovie.vue'
export default {
    props: ['id'],
    components: {
        EditMovie,
    },
    setup(props) {
        const store = useStore();
        
        const movie = ref(null);
        const rating = ref(0);
        const showForm = ref(false);
        
        // Function to fetch movie data
        async function fetchMovieData() {
            try {
                const response = await axios.get(`http://localhost:8000/api/movies/${props.id}/`);
                movie.value = response.data;
            } catch (error) {
                console.log(error);
            }
        }
        
        onMounted(async () => {
            
            await fetchMovieData();
            
        });
        
        
        
        
        
        async function postRating() {
            const filmId = props.id; 
            store.dispatch('updateRating', { movieId:filmId, rating: rating.value });
            await fetchMovieData();
            rating.value = 0;
        }
        
        const editMovie = async (movie) => {
            const filmId = props.id; 
            store.dispatch('editMovie', { movieId:filmId, title: movie.movie.title, description: movie.movie.description });
            movie.value = movie.movie
            await fetchMovieData();
            
            showForm.value = false;
        };
        
        const displayForm = () => {
            console.log(showForm.value);
            showForm.value = !showForm.value;
        }
        
        
        return {
            movie,
            rating,
            showForm,
            postRating,
            editMovie,
            displayForm,
        };
    },
};
</script>

<template>
    <v-form @submit.prevent="updateMovie">
        <v-container>
            <!-- Input fields to edit the movie data -->
            <v-text-field v-model="movie.movie.title" label="Title"></v-text-field>
            <v-text-field v-model="movie.movie.description" label="Description"></v-text-field>
            <!-- Add other input fields here as needed -->
            
            <v-btn @click="updateMovie"  color="primary">Save Changes</v-btn>
        </v-container>
    </v-form>
</template>

<script>
import { reactive, toRefs } from 'vue';

export default {
    props: {
        movie: {
            type: Object,
            required: true,
        },
    },
    
    setup(props, context) {
        const editedMovie = reactive({ ...props.movie });
        
        const updateMovie = () => {
            context.emit('add', editedMovie);
        };
        
        return { ...toRefs(editedMovie), updateMovie };
    },
};
</script>

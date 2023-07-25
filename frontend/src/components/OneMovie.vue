<template>
    <v-card
    class="mx-auto"
    max-width="344"
    >
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
    
    
</v-card>
</template>


<script>
export default {
    props: ['movie'],
    methods: {
        deleteOne(id) {
            this.$emit('delete', id);
        },
    },
};
</script>

<style scoped>
/* Add any custom styles here */
</style>

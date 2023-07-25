import { createStore } from 'vuex';
import axios from 'axios'





const store = createStore({

    state: {



    },

    mutations: {



    },

    actions: {






        updateRating({ commit }, data) {
            console.log(data)
            return axios.post(`http://127.0.0.1:8000/api/movies/${data.movieId}/reviews/`, {
                grade: data.rating,
            })

            .then((res) => {
                return {
                    success: true
                }

            }).catch((err) => {

                return {
                    success: false,
                    error: err

                }

            });

        },

        editMovie({ commit }, data) {

            return axios.put(`http://127.0.0.1:8000/api/movies/${data.movieId}/`, {
                    title: data.title,
                    description: data.description
                })
                .then((res) => {
                    return {
                        success: true
                    }
                }).catch((err) => {
                    return {
                        success: false,
                        error: err
                    }
                });
        },
    },

    getters: {



    }

});




export default store;
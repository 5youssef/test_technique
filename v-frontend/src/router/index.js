// Composables
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import MovieDetail from '../components/MovieDetail.vue'

const routes = [{
        path: '/',
        component: () =>
            import ('@/layouts/default/Default.vue'),
        children: [{
            path: '',
            name: 'Home',
            // route level code-splitting
            // this generates a separate chunk (about.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () =>
                import ( /* webpackChunkName: "home" */ '@/views/Home.vue'),
        }, ],
    },
    {
        path: '/movie',
        name: 'movie',
        component: Home
    },
    {
        path: '/movie/:id',
        name: 'show-movie',
        component: MovieDetail,
        props: true,
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
})

export default router
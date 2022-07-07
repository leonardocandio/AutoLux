import {createRouter, createWebHistory} from 'vue-router'
import {clearUser, getUser} from "@/store";


const routes = [
    {
        path: '/',
        name: 'home',
        component: () => import('../views/HomeView.vue'),
        meta: {requiresAuth: false}
    },
    {
        path: '/login',
        name: 'login',
        component: () => import('../views/AuthView.vue'),
        meta: {requiresAuth: false}
    },
    {
        path: '/logout',
        name: 'logout',
        beforeEnter(to, from, next) {
            fetch('/users/session', {'method': 'DELETE'}).then(r => {
                if (r.status === 200) {
                    clearUser();
                    return next('/');
                }
            })
        },
        meta: {requiresAuth: true}
    },
    {
        path: "/register",
        name: "register",
        component: () => import('../views/AuthView.vue'),
        meta: {requiresAuth: false}
    },
    {
        path: '/forum',
        name: 'forum',
        component: () => import('../views/ForumView.vue'),
        meta: {requiresAuth: false}
    },
    {
        path: '/forum/:id',
        name: 'post-details',
        component: () => import('../views/ForumDetailView.vue'),
        props: true,
        meta: {requiresAuth: true}
    },
    {
        path: '/forum/new',
        name: 'new-post',
        component: () => import('../views/ForumNewView.vue'),
        props: true,
        meta: {requiresAuth: true}
    },
    {
        path: '/profile/:id',
        name: 'profile',
        component: () => import('../views/ProfileView.vue'),
        props: true,
        meta: {requiresAuth: true}
    },
    {
        path: '/shop',
        name: 'shop',
        component: () => import('../views/ShopView.vue'),
        meta: {requiresAuth: false}
    },
    {
        path: '/shop/:id',
        name: 'car-details',
        component: () => import('../views/CarDetailView.vue'),
        meta: {requiresAuth: false}
    }

]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL), routes
})

router.beforeEach(async (to) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        const user = await getUser;
        if (!user) {
            return router.push('/login');
        }
    }
})
export default router

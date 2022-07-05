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
            fetch('/logout', {'method': 'GET'}).then(r => {
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

]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL), routes
})

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (Object.keys(getUser).length === 0) {
            next({
                name: 'login',
                query: {redirect: to.fullPath}
            })
        } else {
            next()
        }
    } else {
        next()
    }
})
export default router

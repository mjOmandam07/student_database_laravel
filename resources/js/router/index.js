import { createRouter, createWebHistory} from 'vue-router'
import Home from '../views/Home.vue'
import College from '../views/College.vue'
import Courses from '../views/Courses.vue'
import AddStudent from '../views/AddStudent.vue'


const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
        props:{
            banner: "Student List"
        }
    },
    {
        path: '/AddStudent',
        name: 'Add Student',
        component: AddStudent,
        props:{
            banner: "Add Student"
        }
    },
    {
        path: '/colleges',
        name: 'Colleges',
        component: College,
        props:{
            banner: "Colleges"
        }
    },
    {
        path: '/courses/:college',
        name: 'Courses',
        component: Courses
    },
]


const router = createRouter({
    history: createWebHistory(),
    routes: routes,
});


export default router
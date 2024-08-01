<template>
    <div class="w-1/6 h-screen flex flex-col overflow-hidden custom-sidebar shadow-lg">
        <h1 class="text-4xl m-8 justify-center text-center font-semibold text-blue-500">Quizit</h1>
        <a-menu class="h-full overflow-auto flex flex-col text-lg pb-10 " v-model:openKeys="state.openKeys"
            v-model:selectedKeys="state.selectedKeys" mode="inline">
            <a-menu-item key="schedule" class="ml-4">
                <router-link :to="{name: 'teacher-schedule'}" class="pl-8">
                    <fa :icon="['far', 'calendar-days']" class="pr-2" />
                    Lịch thi
                </router-link>
            </a-menu-item>

            <a-menu-item key="grade a">
                <router-link :to="{name: 'teacher-group'}" class="pl-8">
                    <fa :icon="['fas', 'graduation-cap']" />
                    Nhóm
                </router-link>
            </a-menu-item>

            <a-menu-item key="quizzes">
                <router-link :to="{name: 'teacher-quizes'}" class="pl-8">
                    <fa :icon="['far', 'question-circle']" />
                    Bộ sưu tập
                </router-link>
            </a-menu-item>

            <a-menu-item key="logout" class="" @click="logout">
                <router-link to="/login" class="pl-8">
                    <fa icon="fa-solid fa-right-from-bracket" /> Đăng xuất
                </router-link>
            </a-menu-item>
        </a-menu>
    </div>
</template>
<script lang="ts" setup>
    import { reactive, watch, h } from 'vue';
import { useRouter } from 'vue-router';

   
    const state = reactive({
       
        selectedKeys: ['1'],
        openKeys: ['sub1'],
        
    });
    
    const logout = () => {
        const router = useRouter()
        localStorage.removeItem('token');
        router.push('/login');
    }
   
</script>

<style>

</style>
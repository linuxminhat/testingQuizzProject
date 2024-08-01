<template>
    <div class="w-1/6 h-screen flex flex-col overflow-hidden custom-sidebar shadow-lg">
        <h1 class="text-4xl m-8 justify-center text-center font-semibold text-blue-500">Quizit</h1>
        <a-menu class="h-full overflow-auto flex flex-col text-lg pb-10 " v-model:openKeys="state.openKeys"
            v-model:selectedKeys="state.selectedKeys" mode="inline">
            <a-menu-item key="schedule" class="ml-4">
                <router-link :to="{name: 'student - schedule'}" class="pl-8">
                    <fa :icon="['far', 'calendar-days']" class="pr-2" />
                    Lịch thi
                </router-link>
            </a-menu-item>

            <a-menu-item key="grade a">
                <router-link :to="{name: 'student - group'}" class="pl-8">
                    <fa :icon="['fas', 'graduation-cap']" />
                    Nhóm
                </router-link>
            </a-menu-item>
            <!-- <a-menu-item key="notif">
                <router-link :to="{name: 'student - notif'}" class="pl-8">
                    <fa icon="fa-solid fa-bell" />
                    Thông báo
                </router-link>
            </a-menu-item> -->

            <a-menu-item key="logout" class="pl-8" @click="logout">
                <router-link to="" class="pl-8">
                    <fa icon="fa-solid fa-right-from-bracket" /> Đăng xuất
                </router-link>
            </a-menu-item>
        </a-menu>
    </div>
</template>
<script lang="ts" setup>
    import { reactive, watch, h } from 'vue';
    import { useRouter } from 'vue-router';
   
    const router = useRouter();

    const state = reactive({
        selectedKeys: ['1'],
        openKeys: ['sub1'],
    });

    const logout = () => {
        localStorage.removeItem("token");
        localStorage.removeItem("role");
        router.push('/login');
    }
</script>

<style>

</style>
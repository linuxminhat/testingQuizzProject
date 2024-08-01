<template>
    <a-layout class="h-screen">
        <a-layout-sider :width="250">
            <student-sidebar class="w-full h-full" />
        </a-layout-sider>
        <a-layout class="h-full">
            <a-layout-header style="position: relative; background: white;" class="shadow-sm">
                <user-header />
            </a-layout-header>
            <a-layout-content class="m-6 bg-white shadow-sm h-full overflow-auto">
                <router-view />
            </a-layout-content>
        </a-layout>
    </a-layout>
</template>

<script setup>
import userHeader from "../components/header/userHeader.vue";
import studentSidebar from "../components/sidebar/StudentSidebar.vue";
</script>

<style scoped>
.h-screen {
    background-color: #ffffff;
}

.a-layout-sider {
    background-color: #ffffff;
}

.overflow-auto {
    overflow-y: auto;
}
</style>
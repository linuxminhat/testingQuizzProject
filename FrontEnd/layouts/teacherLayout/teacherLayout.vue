<template>
    <a-layout class="h-screen">
        <a-layout-sider :width="250">
            <teacher-sidebar class="w-full" />
        </a-layout-sider>
        <a-layout class="h-full flex-column">
            <a-layout-header style="position: relative; background: white;" class="shadow-sm">
                <user-header />
            </a-layout-header>
            <a-layout-content class="m-6 bg-white shadow-sm flex-grow overflow-auto">
                <router-view />
            </a-layout-content>
        </a-layout>
    </a-layout>
</template>

<script setup>
import userHeader from "../components/header/userHeader.vue";
import teacherSidebar from "../components/sidebar/TeacherSidebar.vue";
</script>

<style scoped>
.h-screen {
    background-color: #ffffff;
}

.a-layout-sider {
    background-color: #ffffff;
}

.flex-column {
    display: flex;
    flex-direction: column;
}

.flex-grow {
    flex-grow: 1;
}

.overflow-auto {
    overflow-y: auto;
}
</style>
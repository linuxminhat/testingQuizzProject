<template>
    <div class="fixed top-0 p-4 left-0 flex justify-between items-start w-full shadow-md">
        <div class="relative left-12 hover:cursor-pointer">
            <router-link to="/">

                <h1 class="text-4xl font-bold text-blue-600 font-sans">Quizit</h1>
            </router-link>
        </div>

        <div class=" relative right-24 space-x-10">
            <router-link to="/" class=" text-gray-500 hover:text-blue-600">Trang chủ</router-link>
            <router-link to="/" class=" text-gray-500 hover:text-blue-600">Liên hệ</router-link>
            <button
                class="bg-transparent border border-gray-400 p-2 rounded text-gray-500 hover:bg-blue-600 hover:text-white">
                <router-link to="/login">Đăng nhập</router-link>

            </button>
            <button class="bg-blue-500 text-white  px-4 py-2 rounded hover:bg-blue-700">
                <router-link to="/register">Đăng ký</router-link>
            </button>
        </div>
    </div>

</template>

<script>
export default {

}
</script>

<style>
</style>
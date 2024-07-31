<template>
    <div class="relative mt-24 bg-white w-full ">
        <div class="grid grid-cols-2 gap-x-4 m-24">
            <div class="col-span-1 flex items-center">
                <h1 class="text-6xl font-bold">Chào mừng bạn đến với Quizit</h1>
            </div>
            <div class="col-span-1 flex justify-end items-center p-24 w-full">
                <img src="../assets/img/image.png" alt="" />
            </div>
        </div>

        <div class="slider blur-sm ">
            <img src="https://www.ifse.ca/wp-content/uploads/2023/07/man-3653346-scaled-2.jpg" alt="">
        </div>
    </div>
    <Footer />
</template>

<script>
import Footer from '../components/Footer.vue';
export default {
    components: { Footer }
}
</script>

<style>

</style>
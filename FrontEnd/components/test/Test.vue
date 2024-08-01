<template>
    <div class="bg-gray-100 p-4 rounded-lg shadow-md m-4 flex items-center">
        <!-- <img :src="student.avatar_path" alt="Avatar" class="w-6 h-6 rounded-full mx-12 mb-4"> -->
        <div class="ml-4">
            <h2 class="text-xl font-bold">{{ test.id }}</h2>
            <p class="text-gray-600">{{ test.email }}</p>
        </div>
    </div>

</template>

<script>
export default {
    props: {
        test: {
            type: Object,
            required: true
        },

    }
}
</script>

<style>

</style>
<template>
    <router-link :to="{ name: 'teacher-question-bank', params: { id: collection.id } }">
        <div
            class="m-4 transform transition duration-300 hover:scale-110 rounded-lg shadow-lg h-44 w-56 hover:shadow-xl bg-white overflow-hidden">
            <!-- <div class="bg-gradient-to-br from-rose-100 via-purple-200 to-purple-200 m-2 h-3/6 rounded-lg">
            <img src="https://ghouse.com.vn/wp-content/uploads/2019/07/ghouse-huongdan-c.jpg" alt="">
        </div> -->

            <div class="px-5 pt-2 flex flex-col h-full overflow-auto space-y-2">
                <h2 class="font-semibold text-xl">{{ collection.name }}</h2>
                <p class="text-sm text-gray-500">Ngày tạo: {{ formattedTimestamp }}</p>
                <div class="flex space-x-2 mt-2">
                    <!-- <router-link :to="{ name: 'teacher-question-bank', params: { id: collection.id } }">
                    <button
                        class="bg-blue-500 cursor-pointer text-white px-4 py-2 rounded-md transition duration-150 hover:bg-blue-700"
                        type="button">
                        Chỉnh sửa
                    </button>
                </router-link> -->

                </div>
            </div>
        </div>
    </router-link>
</template>

<script>
export default {
    props: ['collection'],

    computed: {
        formattedTimestamp() {
            const date = new Date(this.collection.created_timestamp);
            return date.toLocaleString([], { year: '2-digit', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' });
        }
    }
}
</script>

<style>

</style>
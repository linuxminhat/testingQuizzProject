<template>

    <div class="bg-gray-100 shadow-lg rounded-lg p-6 w-64 h-64 m-4">
        <h2 class="text-2xl font-semibold mb-4">{{ test.name }}</h2>

        <p class="font-bold">Ngày tạo: </p>
        <p class="text-gray-700">{{formatDate( test.created_timestamp)}}</p>

    </div>
</template>

<script>
import { format } from 'date-fns';
export default {
    props: {
        test: {
            type: Object,
            required: true
        },

    },
    setup() {
        const formatDate = (date) => {
            return format(new Date(date), 'dd/MM/yyyy - HH:mm');
        }
        return {
            formatDate
        }
    }
}
</script>

<style>

</style>
<template>
    <a-calendar v-model:value="value">
        <template #dateCellRender="{ current }">
            <ul class="events">
                <li v-for="item in getListData(current)" :key="item.content">
                    <a-badge :status="item.type" :text="item.content" />
                </li>
            </ul>
        </template>
        <template #monthCellRender="{ current }">
            <div v-if="getMonthData(current)" class="notes-month">
                <section>{{ getMonthData(current) }}</section>
                <span>Backlog number</span>
            </div>
        </template>
    </a-calendar>
</template>
<script setup>
import { onMounted, ref } from 'vue';
import { useStudentStore } from '../../../stores/modules/student';
const value = ref();
const events = ref([]);
const getListData = (value) => {
    const date = value.format('YYYY-MM-DD');
    const listData = events.value.filter(event => {
        const start = event.start.split('T')[0];
        const end = event.end.split('T')[0];
        return date >= start && date <= end;
    }).map(event => {
        const startTime = event.start.split('T')[1].substring(0, 5); // Extracts the time from the start date
        const endTime = event.end.split('T')[1].substring(0, 5); // Extracts the time from the end date
        return {
            type: 'success',
            content: `${event.name} (${startTime} - ${endTime})` // Displays only the time
        };
    });
    return listData.length ? listData : null;
};

const studentStore = useStudentStore();
onMounted(async () => {
    const start = new Date(2024, 5, 20, 9, 0, 0); // replace with actual start date
    const end = new Date(2024, 5, 25, 9, 0, 0); // replace with actual end date

    const startFormatted = `${start.getFullYear()}-${String(start.getMonth() + 1).padStart(2, '0')}-${String(start.getDate()).padStart(2, '0')}T${String(start.getHours()).padStart(2, '0')}:${String(start.getMinutes()).padStart(2, '0')}:${String(start.getSeconds()).padStart(2, '0')}`;
    const endFormatted = `${end.getFullYear()}-${String(end.getMonth() + 1).padStart(2, '0')}-${String(end.getDate()).padStart(2, '0')}T${String(end.getHours()).padStart(2, '0')}:${String(end.getMinutes()).padStart(2, '0')}:${String(end.getSeconds()).padStart(2, '0')}`;

    const res = await studentStore.getSchedule({ start: startFormatted, end: endFormatted });
    events.value = res.map(item => ({
        name: item.name,
        start: item.start,
        end: item.end,
    }));
});
const getMonthData = value => {
    if (value.month() === 8) {
        return 1394;
    }
};
</script>
<style scoped>
  .events {
    list-style: none;
    margin: 0;
    padding: 0;
  }
  .events .ant-badge-status {
    overflow: hidden;
    white-space: nowrap;
    width: 100%;
    text-overflow: ellipsis;
    font-size: 12px;
  }
  .notes-month {
    text-align: center;
    font-size: 28px;
  }
  .notes-month section {
    font-size: 28px;
  }
  </style>
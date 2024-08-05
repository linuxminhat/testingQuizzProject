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
import { ref } from 'vue';
const value = ref();
const getListData = value => {
    let listData;
    switch (value.date()) {
        case 8:
            listData = [
                {
                    type: 'warning',
                    content: 'Quản lý dự án',
                },
                {
                    type: 'success',
                    content: 'Công nghệ web',
                },
            ];
            break;
        case 10:
            listData = [

                {
                    type: 'error',
                    content: 'Phân tích thiết kế HDt',
                },
            ];
            break;
        case 15:
            listData = [

                {
                    type: 'error',
                    content: 'Lập trình mạng',
                },
                {
                    type: 'success',
                    content: 'Công nghệ phần mồm',
                },
            ];
            break;
        default:
    }
    return listData || [];
};
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
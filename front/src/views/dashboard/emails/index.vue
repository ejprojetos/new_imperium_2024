<template>
    <LayoutDashboard>
        <div class="p-8">
            <h1 class="mb-6 text-4xl font-bold">Emails</h1>
            <EmailList />
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import EmailList from '@/components/baseUi/EmailList.vue';
</script>
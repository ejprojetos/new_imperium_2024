<template>
    <LayoutDashboard>
        <div class="p-8">
            <h1 class="mb-6 text-4xl font-bold">Clínicas</h1>
            <ClinicasList />
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import ClinicasList from '@/components/baseUi/ClinicasList.vue';
import LayoutDashboard from '@/layouts/LayoutDashboard.vue';
</script>

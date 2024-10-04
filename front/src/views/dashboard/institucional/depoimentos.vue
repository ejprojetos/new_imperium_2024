<template>
    <LayoutDashboard>
        <div class="p-8">
            <h1 class="mb-6 text-4xl font-bold">Depoimentos</h1>
            <DepoimentosList />
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import DepoimentosList from '@/components/baseUi/DepoimentosList.vue'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
</script>

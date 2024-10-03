<template>
    <LayoutDashboard>
        <div class="p-8">
            <h1 class="mb-6 text-4xl font-bold">Cadastrar itens do site institucional</h1>
            <InstitucionalList />
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import InstitucionalList from '@/components/baseUi/InstitucionalList.vue'
</script>

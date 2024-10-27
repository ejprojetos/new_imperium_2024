<template>
    <div class="embla" ref="emblaRef">
        <div class="embla__container">
            <div class="embla__slide">Slide 1</div>
            <div class="embla__slide">Slide 2</div>
            <div class="embla__slide">Slide 3</div>
        </div>
    </div>
</template>

<script setup lang="ts">
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { Search } from 'lucide-vue-next'
import { RouterLink } from 'vue-router'

import { onMounted } from 'vue'
import emblaCarouselVue from 'embla-carousel-vue'
import Autoplay from 'embla-carousel-autoplay'

const [emblaRef, emblaApi] = emblaCarouselVue({ loop: false }, [Autoplay()])

onMounted(() => {
    if (emblaApi.value) {
        console.log(emblaApi.value.slideNodes()) // Access API
    }
})
</script>

<style scoped>
.min-h-unset {
    min-height: unset;
    height: unset;
}

.custom-placeholder::placeholder {
    color: #121212;
}
.embla {
    overflow: hidden;
}
.embla__container {
    display: flex;
}
.embla__slide {
    flex: 0 0 100%;
    font-size: 48px;
    min-width: 0;
}
</style>

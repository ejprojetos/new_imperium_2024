<template>
    <div class="embla">
        <div class="embla__viewport" ref="emblaRef">
            <div class="embla__container">
                <div v-for="(slide, index) in slides" :key="index" class="embla__slide">
                    <img
                        class="embla__slide__img"
                        :src="`https://picsum.photos/600/350?v=${index}`"
                        alt="Your alt text" />
                </div>
            </div>
        </div>

        <div class="embla__controls">
            <div class="embla__buttons">
                <PrevButton @click="onPrevButtonClick" :disabled="prevBtnDisabled" />
                <NextButton @click="onNextButtonClick" :disabled="nextBtnDisabled" />
            </div>

            <div class="embla__dots">
                <DotButton
                    v-for="(_, index) in scrollSnaps"
                    :key="index"
                    @click="onDotButtonClick(index)"
                    :class="['embla__dot', { 'embla__dot--selected': index === selectedIndex }]" />
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch, computed } from 'vue'
import useEmblaCarousel from 'embla-carousel-vue'
import Autoplay from 'embla-carousel-autoplay'
import { NextButton, PrevButton } from './EmblaCarouselArrowButtons.vue'
import { DotButton } from './EmblaCarouselDotButton.vue'

const TWEEN_FACTOR_BASE = 0.84

const props = defineProps({
    slides: {
        type: Array,
        default: () => [1, 2, 3, 4, 5]
    },
    options: {
        type: Object,
        default: () => ({ loop: false })
    }
})

const [emblaRef, emblaApi] = useEmblaCarousel(props.options, [Autoplay()])

const tweenFactor = ref(0)
const selectedIndex = ref(0)
const scrollSnaps = ref([])
const prevBtnDisabled = ref(true)
const nextBtnDisabled = ref(true)

const numberWithinRange = (number: number, min: number, max: number) =>
    Math.min(Math.max(number, min), max)

const setTweenFactor = () => {
    if (emblaApi.value) {
        tweenFactor.value = TWEEN_FACTOR_BASE * emblaApi.value.scrollSnapList().length
    }
}

const tweenOpacity = (eventName?: string) => {
    if (!emblaApi.value) return

    const engine = emblaApi.value.internalEngine()
    const scrollProgress = emblaApi.value.scrollProgress()
    const slidesInView = emblaApi.value.slidesInView()
    const isScrollEvent = eventName === 'scroll'

    emblaApi.value.scrollSnapList().forEach((scrollSnap, snapIndex) => {
        let diffToTarget = scrollSnap - scrollProgress
        const slidesInSnap = engine.slideRegistry[snapIndex]

        slidesInSnap.forEach((slideIndex: number) => {
            if (isScrollEvent && !slidesInView.includes(slideIndex)) return

            if (engine.options.loop) {
                engine.slideLooper.loopPoints.forEach((loopItem: any) => {
                    const target = loopItem.target()

                    if (slideIndex === loopItem.index && target !== 0) {
                        const sign = Math.sign(target)

                        if (sign === -1) {
                            diffToTarget = scrollSnap - (1 + scrollProgress)
                        }
                        if (sign === 1) {
                            diffToTarget = scrollSnap + (1 - scrollProgress)
                        }
                    }
                })
            }

            const tweenValue = 1 - Math.abs(diffToTarget * tweenFactor.value)
            const opacity = numberWithinRange(tweenValue, 0, 1).toString()
            emblaApi.value.slideNodes()[slideIndex].style.opacity = opacity
        })
    })
}

const onSelect = () => {
    if (!emblaApi.value) return
    selectedIndex.value = emblaApi.value.selectedScrollSnap()
    prevBtnDisabled.value = !emblaApi.value.canScrollPrev()
    nextBtnDisabled.value = !emblaApi.value.canScrollNext()
}

const onPrevButtonClick = () => emblaApi.value?.scrollPrev()
const onNextButtonClick = () => emblaApi.value?.scrollNext()
const onDotButtonClick = (index: number) => emblaApi.value?.scrollTo(index)

watch(emblaApi, (api) => {
    if (!api) return

    scrollSnaps.value = api.scrollSnapList()
    setTweenFactor()
    tweenOpacity()

    api.on('select', onSelect)
    api.on('reInit', setTweenFactor)
    api.on('reInit', tweenOpacity)
    api.on('scroll', tweenOpacity)
    api.on('slideFocus', tweenOpacity)

    onSelect()
})

onMounted(() => {
    if (emblaApi.value) {
        setTweenFactor()
        tweenOpacity()
    }
})
</script>

<style scoped>
.embla {
    overflow: hidden;
}
.embla__container {
    display: flex;
}
.embla__slide {
    flex: 0 0 100%;
    min-width: 0;
}
/* Add more styles as needed */
</style>

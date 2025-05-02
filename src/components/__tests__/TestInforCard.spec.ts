import { mount } from '@vue/test-utils'
import { describe, it, expect } from 'vitest'
import InforCard from '@/components/InforCard.vue'

describe('InforCard.vue', () => {
  it('renders with default props', () => {
    const wrapper = mount(InforCard)

    // Check default classes
    expect(wrapper.find('.card').classes()).toContain('shadow-sm')
    expect(wrapper.find('.card-body').exists()).toBe(true)
    expect(wrapper.find('.card-header').exists()).toBe(false)
  })

  it('renders with custom class props', () => {
    const wrapper = mount(InforCard, {
      props: {
        cardClass: 'text-center',
        bodyClass: 'p-5',
      },
    })

    expect(wrapper.find('.card').classes()).toContain('text-center')
    expect(wrapper.find('.card-body').classes()).toContain('p-5')
  })

  it('renders title when provided', () => {
    const title = 'Test Title'
    const wrapper = mount(InforCard, {
      props: { title },
    })

    expect(wrapper.find('.card-header').exists()).toBe(true)
    expect(wrapper.find('.card-header h5').text()).toBe(title)
    expect(wrapper.find('.card-header').classes()).toContain('py-3')
  })

  it('renders with custom header class', () => {
    const wrapper = mount(InforCard, {
      props: {
        title: 'Title',
        headerClass: 'align-items-end',
      },
    })

    expect(wrapper.find('.card-header').classes()).toContain('align-items-end')
  })

  it('renders slot content', () => {
    const slotContent = '<div class="test-content">Test Slot Content</div>'
    const wrapper = mount(InforCard, {
      slots: {
        default: slotContent,
      },
    })

    expect(wrapper.find('.card-body .test-content').exists()).toBe(true)
    expect(wrapper.find('.test-content').text()).toBe('Test Slot Content')
  })
})

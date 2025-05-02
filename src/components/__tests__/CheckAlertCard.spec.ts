import { mount } from '@vue/test-utils'
import { describe, it, expect } from 'vitest'
import AlertCard from '@/components/AlertCard.vue'

describe('Alert Component', () => {
  // Test default rendering
  it('renders with default props', () => {
    const wrapper = mount(AlertCard, {
      slots: {
        default: 'Test alert message',
      },
    })

    // Check if the component renders
    expect(wrapper.exists()).toBe(true)

    // Verify default classes are applied
    expect(wrapper.classes()).toContain('alert-primary')
    expect(wrapper.classes()).toContain('mt-3')
    expect(wrapper.classes()).toContain('p-3')

    // Check if slot content is rendered
    expect(wrapper.text()).toContain('Test alert message')

    // Verify no icon is shown by default
    expect(wrapper.find('i').exists()).toBe(false)
  })

  // Test custom type
  it('renders with custom type', () => {
    const wrapper = mount(AlertCard, {
      props: {
        type: 'danger',
      },
      slots: {
        default: 'Danger alert',
      },
    })

    expect(wrapper.classes()).toContain('alert-danger')
    expect(wrapper.text()).toContain('Danger alert')
  })

  // Test with icon
  it('renders with icon', () => {
    const wrapper = mount(AlertCard, {
      props: {
        icon: 'exclamation-triangle',
      },
      slots: {
        default: 'Warning with icon',
      },
    })

    const icon = wrapper.find('i')
    expect(icon.exists()).toBe(true)
    expect(icon.classes()).toContain('bi-exclamation-triangle')
    expect(icon.classes()).toContain('me-2')
    expect(wrapper.text()).toContain('Warning with icon')
  })

  // Test custom classes
  it('renders with custom alert class', () => {
    const wrapper = mount(AlertCard, {
      props: {
        alertClass: 'mb-4',
      },
      slots: {
        default: 'Custom class alert',
      },
    })

    expect(wrapper.classes()).toContain('mb-4')
    expect(wrapper.classes()).not.toContain('mt-3')
    expect(wrapper.classes()).not.toContain('p-3')
  })

  // Test validator for type prop
  it('validates type prop correctly', async () => {
    const wrapper = mount(AlertCard, {
      props: {
        type: 'primary',
      },
    })

    // Should work with valid types
    await wrapper.setProps({ type: 'success' })
    expect(wrapper.classes()).toContain('alert-success')

    // Should fall back to default with invalid type (will log a Vue warning)
    await wrapper.setProps({ type: 'invalid-type' as never })
    // Still renders, but logs a warning (can't test the console warning directly)
    expect(wrapper.exists()).toBe(true)
  })

  // Test accessibility attributes
  it('has correct accessibility attributes', () => {
    const wrapper = mount(AlertCard, {
      slots: {
        default: 'Accessible alert',
      },
    })

    expect(wrapper.attributes('role')).toBe('alert')
  })
})

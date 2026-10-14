{{ 'component-cart.css' | asset_url | stylesheet_tag }}
{{ 'component-totals.css' | asset_url | stylesheet_tag }}
{{ 'component-price.css' | asset_url | stylesheet_tag }}
{{ 'component-discounts.css' | asset_url | stylesheet_tag }}

{%- style -%}
  .section-{{ section.id }}-padding {
    padding-top: {{ section.settings.padding_top | times: 0.75 | round: 0 }}px;
    padding-bottom: {{ section.settings.padding_bottom | times: 0.75 | round: 0 }}px;
  }

  @media screen and (min-width: 750px) {
    .section-{{ section.id }}-padding {
      padding-top: {{ section.settings.padding_top }}px;
      padding-bottom: {{ section.settings.padding_bottom }}px;
    }
  }

  /* -------------------------------
     Gift-wrap trigger
  -------------------------------- */
  #main-cart-footer .asl-cart-giftwrap-trigger-wrap {
    width: 100%;
    margin: 0 0 18px;
    padding: 0 0 18px;
    border-bottom: 1px solid rgba(8, 4, 76, 0.18);
  }

  #main-cart-footer .asl-cart-giftwrap-trigger {
    appearance: none;
    -webkit-appearance: none;
    display: inline-flex;
    align-items: center;
    gap: 10px;
    margin: 0;
    padding: 0;
    border: 0;
    background: transparent;
    color: #08044C;
    font: inherit;
    font-size: 15px;
    line-height: 1.25;
    font-weight: 600;
    text-decoration: underline;
    text-underline-offset: 3px;
    cursor: pointer;
  }

  #main-cart-footer .asl-cart-giftwrap-trigger__icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    flex: 0 0 auto;
  }

  /* -------------------------------
     Gift-wrap modal
  -------------------------------- */
  #AslGiftWrapModal-{{ section.id }} {
    position: fixed;

    /* Keep the gift bag drawer BELOW the complete visible store header
       (announcement bar + main header). JS updates this variable on open. */
    top: var(--asl-giftwrap-header-offset, 0px);
    right: 0;
    bottom: 0;
    left: 0;

    height: auto;
    max-height: calc(100dvh - var(--asl-giftwrap-header-offset, 0px));

    z-index: 99999;
    display: none;
  }

  #AslGiftWrapModal-{{ section.id }}.is-open {
    display: block;
  }

  #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-modal__overlay {
    position: absolute;
    inset: 0;
    background: rgba(0, 0, 0, 0.35);
  }

  #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-modal__panel {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;

    width: min(820px, 100%);
    height: auto;
    max-height: 100%;

    background: #fff;
    color: #08044C;
    overflow-y: auto;
    overscroll-behavior: contain;
    -webkit-overflow-scrolling: touch;

    box-shadow: -12px 0 34px rgba(0, 0, 0, 0.12);
  }

  #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-modal__inner {
    min-height: 100%;
    display: flex;
    flex-direction: column;
    padding: 28px 22px 20px;
    box-sizing: border-box;
  }

  #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-modal__close {
    position: absolute;
    top: 18px;
    right: 18px;
    z-index: 2;
    width: 42px;
    height: 42px;
    padding: 0;
    border: 0;
    background: transparent;
    color: #08044C;
    font-size: 34px;
    line-height: 1;
    font-weight: 300;
    cursor: pointer;
  }

  #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-modal__title {
    margin: 0 58px 24px 0;
    color: #08044C;
    font-size: 30px;
    line-height: 1.1;
    font-weight: 700;
  }

  #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-modal__description {
    margin: -10px 0 22px;
    color: rgba(8, 4, 76, 0.72);
    font-size: 14px;
    line-height: 1.45;
  }

  #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-modal__variants {
    margin: 0 0 22px;
  }

  #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-variant {
    display: grid;
    grid-template-columns: minmax(0, 1fr) auto;
    align-items: center;
    gap: 18px;
    min-height: 58px;
    padding: 7px 0;
    border-bottom: 1px solid rgba(8, 4, 76, 0.08);
  }

  #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-variant:last-child {
    border-bottom: 0;
  }

  #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-variant__info {
    display: flex;
    align-items: center;
    gap: 12px;
    min-width: 0;
  }

  #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-variant__thumb {
    width: 50px;
    height: 60px;
    flex: 0 0 auto;
    object-fit: contain;
    background: #f4f4f4;
    mix-blend-mode: multiply;
  }

  #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-variant__text {
    min-width: 0;
  }

  #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-variant__name {
    display: block;
    margin-bottom: 2px;
    color: #08044C;
    font-size: 16px;
    line-height: 1.25;
    font-weight: 600;
  }

  #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-variant__price {
    display: block;
    color: rgba(8, 4, 76, 0.65);
    font-size: 13px;
    line-height: 1.25;
  }

  #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-qty {
    display: grid;
    grid-template-columns: 34px 38px 34px;
    align-items: center;
  }

  #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-qty__button {
    appearance: none;
    -webkit-appearance: none;
    width: 34px;
    height: 34px;
    padding: 0;
    border: 0;
    background: transparent;
    color: #08044C;
    font-size: 20px;
    line-height: 1;
    cursor: pointer;
  }

  #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-qty__input {
    width: 38px;
    height: 34px;
    padding: 0;
    border: 0;
    background: transparent;
    color: #08044C;
    text-align: center;
    font: inherit;
    font-size: 15px;
    appearance: textfield;
    -moz-appearance: textfield;
  }

  #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-qty__input::-webkit-inner-spin-button,
  #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-qty__input::-webkit-outer-spin-button {
    -webkit-appearance: none;
    margin: 0;
  }

  #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-modal__hero {
    width: 100%;
    margin: 0 0 20px;
    background: #f2f2f2;
    overflow: hidden;
  }

  #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-modal__hero img {
    display: block;
    width: 100%;
    height: min(42vw, 430px);
    min-height: 280px;
    object-fit: contain;
    object-position: center;
    mix-blend-mode: multiply;
  }

  #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-modal__footer {
    position: sticky;
    bottom: 0;
    display: grid;
    grid-template-columns: 245px minmax(0, 1fr);
    gap: 10px;
    margin-top: auto;
    padding-top: 12px;
    background: #fff;
  }

  #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-modal__total {
    min-height: 52px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 7px;
    border: 1px solid #08044C;
    color: #08044C;
    font-size: 15px;
    line-height: 1;
  }

  #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-modal__add {
    min-height: 52px;
    padding: 0 20px;
    border: 1px solid #08044C;
    border-radius: 0;
    background: #08044C;
    color: #fff;
    font: inherit;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
  }

  #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-modal__add:disabled {
    background: #aaa;
    border-color: #aaa;
    cursor: not-allowed;
  }

  #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-modal__error {
    margin: 10px 0 0;
    padding: 10px 12px;
    border: 1px solid rgba(160, 0, 0, .24);
    background: rgba(160, 0, 0, .06);
    color: #8a0000;
    font-size: 12px;
    line-height: 1.4;
  }

  body.asl-giftwrap-open {
    overflow: hidden !important;
  }

  @media screen and (max-width: 749px) {
    #main-cart-footer .asl-cart-giftwrap-trigger-wrap {
      margin-bottom: 14px;
      padding-bottom: 14px;
    }

    #main-cart-footer .asl-cart-giftwrap-trigger {
      font-size: 14px;
    }

    #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-modal__panel {
      width: 100%;
    }

    #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-modal__inner {
      padding: 22px 15px 14px;
    }

    #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-modal__close {
      top: 12px;
      right: 10px;
    }

    #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-modal__title {
      margin-right: 50px;
      margin-bottom: 20px;
      font-size: 23px;
    }

    #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-variant {
      gap: 8px;
    }

    #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-variant__thumb {
      width: 42px;
      height: 52px;
    }

    #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-variant__name {
      font-size: 14px;
    }

    #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-modal__hero img {
      height: 42vh;
      min-height: 250px;
    }

    #AslGiftWrapModal-{{ section.id }} .asl-giftwrap-modal__footer {
      grid-template-columns: 1fr;
    }
  }

  /* =========================================================
     PAYMENT METHODS BELOW CHECKOUT
  ========================================================= */
  #main-cart-footer .asl-checkout-payment-methods {
    width: 100%;
    margin: 14px 0 0;
  }

  #main-cart-footer .asl-checkout-payment-methods__label {
    margin: 0 0 9px;
    color: rgba(8, 4, 76, .68);
    font-size: 11px;
    line-height: 1.2;
    letter-spacing: .08em;
    text-align: center;
    text-transform: uppercase;
  }

  #main-cart-footer .asl-checkout-payment-methods__icons {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
    gap: 7px;
    width: 100%;
  }

  #main-cart-footer .asl-checkout-payment-method {
    display: inline-flex;
    align-items: center;
    justify-content: center;

    min-width: 0;
    height: auto;
    padding: 0;

    border: 0;
    border-radius: 0;
    background: transparent;

    box-sizing: border-box;
  }

  #main-cart-footer .asl-checkout-payment-method svg {
    display: block;
    width: auto;
    max-width: 48px;
    height: 24px;
  }

  @media screen and (max-width: 749px) {
    #main-cart-footer .asl-checkout-payment-methods {
      margin-top: 12px;
    }

    #main-cart-footer .asl-checkout-payment-methods__icons {
      gap: 6px;
    }

    #main-cart-footer .asl-checkout-payment-method {
      min-width: 0;
      height: auto;
      padding: 0;
    }

    #main-cart-footer .asl-checkout-payment-method svg {
      max-width: 44px;
      height: 22px;
    }
  }


  /* =========================================================
     CART PAGE — DESKTOP TWO COLUMN LAYOUT
     LEFT: products
     RIGHT: apps / note / subtotal / checkout
  ========================================================= */

  @media screen and (min-width: 990px) {
    .asl-cart-page-layout {
      display: grid !important;
      grid-template-columns: minmax(0, 2.05fr) minmax(360px, .95fr) !important;
      column-gap: clamp(44px, 5vw, 82px) !important;
      align-items: start !important;

      width: 100% !important;
      max-width: 1660px !important;

      margin: 0 auto !important;
      padding: 44px 52px 72px !important;

      box-sizing: border-box !important;
    }

    .asl-cart-page-layout > .shopify-section {
      min-width: 0 !important;
      margin: 0 !important;
    }

    .asl-cart-page-layout #main-cart-footer {
      width: 100% !important;
      min-width: 0 !important;

      margin: 0 !important;
      padding: 0 !important;

      background: transparent !important;
    }

    .asl-cart-page-layout #main-cart-footer > .page-width {
      width: 100% !important;
      max-width: none !important;

      margin: 0 !important;
      padding: 0 !important;
    }

    .asl-cart-page-layout #main-cart-footer .cart__footer {
      display: block !important;

      width: 100% !important;
      max-width: none !important;

      margin: 0 !important;
      padding: 0 !important;
    }

    .asl-cart-page-layout #main-cart-footer .cart__note,
    .asl-cart-page-layout #main-cart-footer .cart__blocks,
    .asl-cart-page-layout #main-cart-footer .cart__ctas,
    .asl-cart-page-layout #main-cart-footer .cart__dynamic-checkout-buttons {
      width: 100% !important;
      max-width: none !important;
    }

    .asl-cart-page-layout #main-cart-footer .cart__note {
      margin: 0 0 16px !important;
    }

    .asl-cart-page-layout #main-cart-footer .cart__blocks {
      display: flex !important;
      flex-direction: column !important;
      gap: 16px !important;
    }

    /* App blocks fill the summary column */
    .asl-cart-page-layout #main-cart-footer .cart__blocks > .shopify-app-block,
    .asl-cart-page-layout #main-cart-footer .cart__blocks > [data-shopify-editor-block] {
      width: 100% !important;
      max-width: none !important;
    }

    /* Subtotal row */
    .asl-cart-page-layout #main-cart-footer .totals {
      display: flex !important;
      align-items: baseline !important;
      justify-content: space-between !important;
      gap: 24px !important;

      width: 100% !important;
      margin: 4px 0 0 !important;
    }

    .asl-cart-page-layout #main-cart-footer .totals__total,
    .asl-cart-page-layout #main-cart-footer .totals__total-value {
      margin: 0 !important;
      font-size: 18px !important;
      line-height: 1.2 !important;
      font-weight: 650 !important;
    }

    .asl-cart-page-layout #main-cart-footer .tax-note {
      display: block !important;
      margin-top: 8px !important;
      text-align: left !important;
    }

    /* Checkout */
    .asl-cart-page-layout #main-cart-footer #checkout {
      width: 100% !important;
      min-height: 50px !important;

      margin: 0 !important;

      border-radius: 999px !important;
      background: #08044C !important;
      color: #fff !important;

      font-size: 14px !important;
      font-weight: 600 !important;
    }

    .asl-cart-page-layout #main-cart-footer .asl-cart-giftwrap-trigger-wrap {
      margin: 0 !important;
      padding: 0 0 16px !important;
    }

    .asl-cart-page-layout #main-cart-footer .asl-checkout-payment-methods {
      margin-top: 4px !important;
    }
  }

  @media screen and (max-width: 989px) {
    .asl-cart-page-layout {
      display: block !important;
    }
  }

  /* Keep the footer target in the DOM for Dawn AJAX updates,
     but visually remove it when the cart is empty. */
  #main-cart-footer.is-empty {
    display: none !important;
    margin: 0 !important;
    padding: 0 !important;
  }

  /* Square checkout buttons. Dawn uses radius variables + pseudo elements. */
  #main-cart-footer {
    --buttons-radius: 0px !important;
    --buttons-radius-outset: 0px !important;
  }

  #main-cart-footer #checkout,
  #main-cart-footer #checkout-klarna,
  #main-cart-footer .cart__checkout-button,
  #main-cart-footer .cart__ctas .button {
    border-radius: 0 !important;
  }

  #main-cart-footer #checkout::before,
  #main-cart-footer #checkout::after,
  #main-cart-footer #checkout-klarna::before,
  #main-cart-footer #checkout-klarna::after,
  #main-cart-footer .cart__checkout-button::before,
  #main-cart-footer .cart__checkout-button::after,
  #main-cart-footer .cart__ctas .button::before,
  #main-cart-footer .cart__ctas .button::after {
    border-radius: 0 !important;
  }

{%- endstyle -%}

{%- assign gift_bag_count = 0 -%}
{%- for block in section.blocks -%}
  {%- if block.type == 'gift_bag_small' or block.type == 'gift_bag_medium' -%}
    {%- if block.settings.product != blank -%}
      {%- assign gift_bag_count = gift_bag_count | plus: 1 -%}
    {%- endif -%}
  {%- endif -%}
{%- endfor -%}

<div
  class="gradient color-{{ section.settings.color_scheme }}{% if cart == empty %} is-empty{% endif %}"
  id="main-cart-footer"
  data-id="{{ section.id }}"
>
  <div class="page-width">
    <div class="cart__footer isolate section-{{ section.id }}-padding">
      {%- if settings.show_cart_note -%}
        <details class="asl-cart-accordion asl-cart-note-accordion">
          <summary class="asl-cart-accordion__summary">
            <span>{{ 'sections.cart.note' | t }}</span>

            <span class="asl-cart-accordion__icon" aria-hidden="true">
              <svg viewBox="0 0 16 16">
                <path d="M3 6l5 5 5-5"/>
              </svg>
            </span>
          </summary>

          <div class="asl-cart-accordion__content">
            <cart-note class="cart__note field">
              <label class="visually-hidden" for="Cart-note">
                {{ 'sections.cart.note' | t }}
              </label>

              <textarea
                class="text-area field__input"
                name="note"
                form="cart"
                id="Cart-note"
                placeholder="{{ 'sections.cart.note' | t }}"
              >{{ cart.note }}</textarea>
            </cart-note>
          </div>
        </details>
      {%- endif -%}

      {%- if gift_bag_count > 0 -%}
        <div class="asl-cart-giftwrap-trigger-wrap">
          <button
            type="button"
            class="asl-cart-giftwrap-trigger"
            id="AslGiftWrapOpen-{{ section.id }}"
            aria-haspopup="dialog"
            aria-controls="AslGiftWrapModal-{{ section.id }}"
          >
            <span class="asl-cart-giftwrap-trigger__icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.4">
                <path d="M20 12v9H4v-9M2 7h20v5H2zM12 7v14M12 7H7.5A2.5 2.5 0 1 1 10 4.5C10 6 12 7 12 7Zm0 0h4.5A2.5 2.5 0 1 0 14 4.5C14 6 12 7 12 7Z"/>
              </svg>
            </span>
            <span>{{ section.settings.gift_wrap_trigger_text }}</span>
          </button>
        </div>
      {%- endif -%}

      <div class="cart__blocks">



        {% for block in section.blocks %}
          {%- case block.type -%}
            {%- when '@app' -%}
              {% render block %}
            {%- when 'subtotal' -%}
              <div class="js-contents" {{ block.shopify_attributes }}>
                <div>
                  {%- if cart.cart_level_discount_applications.size > 0 -%}
                    <ul class="discounts list-unstyled" role="list" aria-label="{{ 'customer.order.discount' | t }}">
                      {%- for discount in cart.cart_level_discount_applications -%}
                        <li class="discounts__discount discounts__discount--position">
                          {{- 'icon-discount.svg' | inline_asset_content -}}
                          {{ discount.title | escape }}
                          (-{{ discount.total_allocated_amount | money }})
                        </li>
                      {%- endfor -%}
                    </ul>
                  {%- endif -%}
                </div>

                <div class="totals">
                  <h2 class="totals__total">{{ 'sections.cart.estimated_total' | t }}</h2>
                  <p class="totals__total-value">{{ cart.total_price | money_with_currency }}</p>
                </div>

                <small class="tax-note caption-large rte">
                  {%- if cart.duties_included and cart.taxes_included -%}
                    {%- if shop.shipping_policy.body == blank -%}
                      {{ 'sections.cart.duties_and_taxes_included_shipping_at_checkout_without_policy' | t }}
                    {%- else -%}
                      {{
                        'sections.cart.duties_and_taxes_included_shipping_at_checkout_with_policy_html'
                        | t: link: shop.shipping_policy.url
                      }}
                    {%- endif -%}
                  {%- elsif cart.duties_included == false and cart.taxes_included -%}
                    {%- if shop.shipping_policy.body == blank -%}
                      {{ 'sections.cart.taxes_included_shipping_at_checkout_without_policy' | t }}
                    {%- else -%}
                      {{
                        'sections.cart.taxes_included_shipping_at_checkout_with_policy_html'
                        | t: link: shop.shipping_policy.url
                      }}
                    {%- endif -%}
                  {%- elsif cart.duties_included and cart.taxes_included == false -%}
                    {%- if shop.shipping_policy.body == blank -%}
                      {{ 'sections.cart.duties_included_taxes_at_checkout_shipping_at_checkout_without_policy' | t }}
                    {%- else -%}
                      {{
                        'sections.cart.duties_included_taxes_at_checkout_shipping_at_checkout_with_policy_html'
                        | t: link: shop.shipping_policy.url
                      }}
                    {%- endif -%}
                  {%- elsif cart.duties_included == false and cart.taxes_included == false -%}
                    {%- if shop.shipping_policy.body == blank -%}
                      {{ 'sections.cart.taxes_at_checkout_shipping_at_checkout_without_policy' | t }}
                    {%- else -%}
                      {{
                        'sections.cart.taxes_at_checkout_shipping_at_checkout_with_policy_html'
                        | t: link: shop.shipping_policy.url
                      }}
                    {%- endif -%}
                  {%- endif -%}
                </small>
              </div>
            {%- when 'buttons' -%}
              <div class="asl-checkout-stack">
              <div class="cart__ctas" {{ block.shopify_attributes }}>
                <button
                  type="submit"
                  id="checkout"
                  class="cart__checkout-button button"
                  name="checkout"
                  {% if cart == empty %}
                    disabled
                  {% endif %}
                  form="cart"
                >
                  {{ 'sections.cart.checkout' | t }}
                </button>
              </div>

              {%- if additional_checkout_buttons -%}
                <div class="cart__dynamic-checkout-buttons additional-checkout-buttons">
                  {{ content_for_additional_checkout_buttons }}
                </div>
              {%- endif -%}

              {%- assign asl_klarna_min_cents = section.settings.klarna_min_cart_amount | times: 100 -%}
              {%- if section.settings.show_klarna_checkout and cart.total_price >= asl_klarna_min_cents -%}
              <div class="cart__ctas cart__ctas--klarna">
                <button
                  type="submit"
                  id="checkout-klarna"
                  class="cart__checkout-button button asl-klarna-checkout"
                  name="checkout"
                  {% if cart == empty %}
                    disabled
                  {% endif %}
                  form="cart"
                  aria-label="Pay with Klarna"
                >
                  <img
                    src="{{ 'klarna-payment-badge.webp' | asset_url }}"
                    alt="Klarna"
                    class="asl-klarna-checkout__logo"
                    width="144"
                    height="61"
                    loading="eager"
                  >
                  <span class="visually-hidden">Pay with Klarna</span>
                </button>
              </div>
              {%- endif -%}

              {%- if section.settings.show_payment_icons -%}
                <div class="asl-checkout-payment-methods">
                  {%- if section.settings.payment_icons_label != blank -%}
                    <p class="asl-checkout-payment-methods__label">
                      {{ section.settings.payment_icons_label }}
                    </p>
                  {%- endif -%}

                  <div class="asl-checkout-payment-methods__icons" aria-label="Accepted payment methods">
                    {%- assign asl_payment_types = 'apple_pay,google_pay,klarna,maestro,master,visa,diners_club,unionpay,netbanking,iris,revolut' | split: ',' -%}

                    {%- for payment_type in asl_payment_types -%}
                      <span class="asl-checkout-payment-method" title="{{ payment_type | replace: '_', ' ' | capitalize }}">
                        {{ payment_type | payment_type_svg_tag }}
                      </span>
                    {%- endfor -%}
                  </div>
                </div>
              {%- endif -%}
              </div>
          {%- endcase -%}
        {% endfor %}

        <div id="cart-errors"></div>
      </div>
    </div>
  </div>
</div>


<!-- Customizable checkout delivery choice. BOX NOW's existing app block is reused. -->
<div id="AslDeliveryModal-{{ section.id }}" class="asl-delivery-modal asl-delivery-modal--center" hidden aria-hidden="true"
 style="--adl-overlay:{{ section.settings.delivery_overlay_color }};--adl-bg:{{ section.settings.delivery_bg }};--adl-text:{{ section.settings.delivery_text_color }};--adl-muted:{{ section.settings.delivery_muted_color }};--adl-accent:{{ section.settings.delivery_accent_color }};--adl-btn-bg:{{ section.settings.delivery_button_bg }};--adl-btn-text:{{ section.settings.delivery_button_text }};--adl-border:{{ section.settings.delivery_border_color }};--adl-radius:{{ section.settings.delivery_radius }}px;--adl-width:{{ section.settings.delivery_width }}px;--adl-pad:{{ section.settings.delivery_padding }}px;--adl-title-size:{{ section.settings.delivery_title_size }}px;--adl-option-gap:{{ section.settings.delivery_option_gap }}px;--adl-overlay-opacity:{{ section.settings.delivery_overlay_opacity | divided_by: 100.0 }};">
  <div class="asl-delivery-modal__shade" data-delivery-close></div>
  <section class="asl-delivery-modal__panel" role="dialog" aria-modal="true" aria-labelledby="AslDeliveryTitle-{{ section.id }}" tabindex="-1">
    <button type="button" class="asl-delivery-modal__close" data-delivery-close aria-label="{{ section.settings.delivery_close_label | escape }}">×</button>
    <h2 id="AslDeliveryTitle-{{ section.id }}">{{ section.settings.delivery_title | escape }}</h2>
    {%- if section.settings.delivery_description != blank -%}<div class="asl-delivery-modal__description rte">{{ section.settings.delivery_description }}</div>{%- endif -%}
    <div class="asl-delivery-modal__main">
      <div class="asl-delivery-modal__left">
    <div class="asl-delivery-modal__options">
      <label class="asl-delivery-modal__option"><input type="radio" name="asl-delivery-method-{{ section.id }}" value="courier"><span class="asl-delivery-carrier-copy"><strong>{{ section.settings.delivery_courier_title | escape }}</strong><small>{{ section.settings.delivery_courier_subtitle | escape }}</small></span>
        <span class="asl-delivery-carrier-logos">
          {%- if section.settings.delivery_courier_logo != blank -%}
            {{ section.settings.delivery_courier_logo | image_url: width: 240 | image_tag: class: 'asl-delivery-carrier-logo', loading: 'lazy', widths: '80,120,180,240', alt: section.settings.delivery_courier_title }}
          {%- endif -%}
          {%- if section.settings.delivery_courier_logo_2 != blank -%}
            <span class="asl-delivery-logo-more" tabindex="0" aria-label="Show additional carrier logo">
              <span class="asl-delivery-logo-plus" aria-hidden="true">+</span>
              <span class="asl-delivery-logo-tooltip" role="img" aria-label="Additional carrier logo">
                {{ section.settings.delivery_courier_logo_2 | image_url: width: 240 | image_tag: class: 'asl-delivery-carrier-logo asl-delivery-carrier-logo--second', loading: 'lazy', widths: '80,120,180,240', alt: section.settings.delivery_courier_title }}
              </span>
            </span>
          {%- endif -%}
        </span></label>
      <label class="asl-delivery-modal__option"><input type="radio" name="asl-delivery-method-{{ section.id }}" value="boxnow"><span class="asl-delivery-carrier-copy"><strong>{{ section.settings.delivery_boxnow_title | escape }}</strong><small>{{ section.settings.delivery_boxnow_subtitle | escape }}</small></span>
        <span class="asl-delivery-carrier-logos">
          {%- if section.settings.delivery_boxnow_logo != blank -%}
            {{ section.settings.delivery_boxnow_logo | image_url: width: 240 | image_tag: class: 'asl-delivery-carrier-logo', loading: 'lazy', widths: '80,120,180,240', alt: section.settings.delivery_boxnow_title }}
          {%- endif -%}
          {%- if section.settings.delivery_boxnow_logo_2 != blank -%}
            <span class="asl-delivery-logo-more" tabindex="0" aria-label="Show additional carrier logo">
              <span class="asl-delivery-logo-plus" aria-hidden="true">+</span>
              <span class="asl-delivery-logo-tooltip" role="img" aria-label="Additional carrier logo">
                {{ section.settings.delivery_boxnow_logo_2 | image_url: width: 240 | image_tag: class: 'asl-delivery-carrier-logo asl-delivery-carrier-logo--second', loading: 'lazy', widths: '80,120,180,240', alt: section.settings.delivery_boxnow_title }}
              </span>
            </span>
          {%- endif -%}
        </span></label>
      <label class="asl-delivery-modal__option"><input type="radio" name="asl-delivery-method-{{ section.id }}" value="acs"><span class="asl-delivery-carrier-copy"><strong>{{ section.settings.delivery_acs_title | escape }}</strong><small>{{ section.settings.delivery_acs_subtitle | escape }}</small></span>
        <span class="asl-delivery-carrier-logos">
          {%- if section.settings.delivery_acs_logo != blank -%}{{ section.settings.delivery_acs_logo | image_url: width: 240 | image_tag: class: 'asl-delivery-carrier-logo', loading: 'lazy', widths: '80,120,180,240', alt: section.settings.delivery_acs_title }}{%- endif -%}
          {%- if section.settings.delivery_acs_logo_2 != blank -%}<span class="asl-delivery-logo-more" tabindex="0" aria-label="Additional ACS logo"><span class="asl-delivery-logo-plus" aria-hidden="true">+</span><span class="asl-delivery-logo-tooltip">{{ section.settings.delivery_acs_logo_2 | image_url: width: 240 | image_tag: class: 'asl-delivery-carrier-logo asl-delivery-carrier-logo--second', loading: 'lazy', widths: '80,120,180,240', alt: section.settings.delivery_acs_title }}</span></span>{%- endif -%}
        </span></label>
    </div>
      </div>
    <div class="asl-delivery-modal__boxnow" data-boxnow-area hidden>
      {%- if section.settings.delivery_map_heading != blank -%}<h3>{{ section.settings.delivery_map_heading | escape }}</h3>{%- endif -%}
      <div class="asl-boxnow-map-slot" aria-label="BOX NOW Locker Map" data-boxnow-mount></div>
      <p class="asl-delivery-modal__error" data-boxnow-missing role="alert" hidden>{{ section.settings.delivery_missing_map | escape }}</p>
      {%- if section.settings.delivery_map_notice != blank -%}<div class="asl-delivery-modal__map-notice">{{ section.settings.delivery_map_notice | escape }}</div>{%- endif -%}
    </div>
    <div class="asl-delivery-modal__acs" data-acs-area hidden>
      <h3>{{ section.settings.delivery_acs_heading | escape }}</h3>
      <p class="asl-delivery-modal__map-notice">{{ section.settings.delivery_acs_help | escape }}</p>
      <label class="asl-acs-label" for="AslAcsSearch-{{ section.id }}">Αναζήτηση πόλης, ΤΚ ή locker</label>
      <input type="search" id="AslAcsSearch-{{ section.id }}" class="asl-acs-search" autocomplete="off" placeholder="{{ section.settings.delivery_acs_search_placeholder | escape }}" data-acs-search>
      <p class="asl-acs-status" data-acs-status aria-live="polite"></p>
      <div class="asl-acs-results" data-acs-results role="group" aria-label="ACS Smartpoint Lockers"></div>
      <div class="asl-acs-selected" data-acs-selected hidden aria-live="polite"></div>
    </div>
    </div>
    <p class="asl-delivery-modal__error" data-delivery-error role="alert" hidden></p>
    <button type="button" class="asl-delivery-modal__continue" data-delivery-continue>{{ section.settings.delivery_continue_text | escape }}</button>
  </section>
</div>
<style>
.asl-delivery-modal[hidden],.asl-delivery-modal [hidden]{display:none!important}
.asl-delivery-modal{position:fixed;inset:0;top:var(--adl-header-offset,0px);z-index:100005;color:var(--adl-text);font-family:inherit}
.asl-delivery-modal__shade{position:absolute;inset:0;background:var(--adl-overlay);opacity:var(--adl-overlay-opacity)}
.asl-delivery-modal__panel{position:absolute;top:0;right:0;bottom:0;width:min(var(--adl-width),100%);background:var(--adl-bg);color:var(--adl-text);overflow-y:auto;box-shadow:-10px 0 32px #0002;padding:var(--adl-pad);box-sizing:border-box;border-radius:var(--adl-radius) 0 0 var(--adl-radius)}
.asl-delivery-modal--center .asl-delivery-modal__panel{top:50%;left:50%;right:auto;bottom:auto;transform:translate(-50%,-50%);width:min(var(--adl-width),calc(100% - 30px));max-height:calc(100dvh - var(--adl-header-offset,0px) - 30px);border-radius:var(--adl-radius)}
.asl-delivery-modal__panel h2{font-size:var(--adl-title-size);margin:0 38px 14px 0;line-height:1.2;color:var(--adl-text)}
.asl-delivery-modal__panel p{font-size:14px;line-height:1.5}
.asl-delivery-modal__description{font-size:14px;line-height:1.5;color:var(--adl-muted)}
.asl-delivery-modal__description p{margin:0 0 10px}
.asl-delivery-modal__close{position:absolute;right:16px;top:12px;border:0;background:none;font-size:36px;color:var(--adl-text);cursor:pointer}
.asl-delivery-modal__options{display:grid;gap:var(--adl-option-gap);margin:24px 0}
.asl-delivery-modal__option{display:flex;align-items:center;gap:15px;border:1px solid var(--adl-border);padding:18px;cursor:pointer;border-radius:var(--adl-radius);background:var(--adl-bg)}
.asl-delivery-modal__option:has(input:checked){outline:2px solid var(--adl-accent);outline-offset:-2px;border-color:var(--adl-accent)}
.asl-delivery-modal__option input{accent-color:var(--adl-accent);width:19px;height:19px;flex:none}
.asl-delivery-modal__option strong,.asl-delivery-modal__option small{display:block}
.asl-delivery-modal__option small{color:var(--adl-muted);margin-top:3px}
/* Optional carrier logos, including an accessible hover/focus/tap + preview. */
.asl-delivery-modal__option .asl-delivery-carrier-copy{flex:1;min-width:0}
.asl-delivery-carrier-logos{display:inline-flex;align-items:center;gap:8px;flex:none;margin-left:auto}
.asl-delivery-carrier-logo{display:block;width:auto;max-width:80px;height:38px;object-fit:contain}
.asl-delivery-logo-more{position:relative;display:inline-flex;align-items:center;justify-content:center;flex:none;width:28px;height:28px;border:1px solid var(--adl-border);border-radius:50%;background:var(--adl-bg);color:var(--adl-text);font-size:19px;font-weight:500;line-height:1;cursor:pointer;outline-offset:3px}
.asl-delivery-logo-tooltip{position:absolute;bottom:calc(100% + 10px);right:-8px;z-index:10;display:flex;align-items:center;justify-content:center;min-width:108px;min-height:60px;padding:10px;border:1px solid var(--adl-border);border-radius:8px;background:var(--adl-bg);box-shadow:0 8px 25px #0002;opacity:0;visibility:hidden;pointer-events:none;transform:translateY(5px);transition:opacity .15s,transform .15s,visibility .15s}
.asl-delivery-logo-more:hover .asl-delivery-logo-tooltip,.asl-delivery-logo-more:focus .asl-delivery-logo-tooltip,.asl-delivery-logo-more:focus-within .asl-delivery-logo-tooltip{opacity:1;visibility:visible;transform:translateY(0)}
.asl-delivery-logo-tooltip .asl-delivery-carrier-logo{max-width:112px;height:48px}
@media(max-width:749px){.asl-delivery-modal__option{gap:9px}.asl-delivery-carrier-logo{max-width:54px;height:30px}.asl-delivery-logo-tooltip{right:0}}

.asl-delivery-modal__boxnow{border-top:1px solid var(--adl-border);padding:16px 0 20px}
.asl-delivery-modal__boxnow h3{font-size:17px;margin:0 0 12px}
.asl-delivery-modal__map-notice{font-size:12px;line-height:1.5;color:var(--adl-muted);margin-top:10px}
.asl-delivery-modal__continue{display:block;width:100%;min-height:51px;padding:12px 15px;border:0;border-radius:var(--adl-radius);background:var(--adl-btn-bg);color:var(--adl-btn-text);font:inherit;font-weight:600;cursor:pointer}
.asl-delivery-modal__continue:disabled{opacity:.55;cursor:wait}
.asl-boxnow-prelaunch{position:fixed!important;left:-100000px!important;top:0!important;width:min(540px,100vw)!important;max-width:540px!important;opacity:0!important;pointer-events:none!important;z-index:-1!important}
.asl-boxnow-prelaunch-section{height:0!important;min-height:0!important;margin:0!important;padding:0!important;border:0!important;overflow:visible!important}
.asl-boxnow-map-slot{min-height:55px;margin:12px 0}.asl-boxnow-map-slot:empty:before{content:"BOX NOW map loading…";font-size:12px;color:var(--adl-muted)}
.asl-delivery-modal__error{color:#9b2020;border:1px solid #dfa3a3;padding:10px}
body.asl-delivery-modal-open{overflow:hidden!important}
/* v7: Always center the delivery popup on desktop, ignoring old theme settings. */
@media screen and (min-width: 750px) {
  #AslDeliveryModal-{{ section.id }} .asl-delivery-modal__panel {
    position: absolute !important;
    top: 50% !important;
    left: 50% !important;
    right: auto !important;
    bottom: auto !important;
    transform: translate(-50%, -50%) !important;
    width: min(var(--adl-width), calc(100vw - 40px)) !important;
    height: auto !important;
    max-height: calc(100dvh - var(--adl-header-offset,0px) - 32px) !important;
    border-radius: var(--adl-radius) !important;
    overflow-y: auto !important;
  }
}

@media(max-width:749px){.asl-delivery-modal__panel{padding:24px 18px}.asl-delivery-modal__panel h2{font-size:min(var(--adl-title-size),26px)}.asl-delivery-modal--center .asl-delivery-modal__panel{top:0;left:auto;right:0;bottom:0;transform:none;width:100%;max-height:100%;border-radius:0}}

/* v9: Two-column delivery choice on desktop, with BOX NOW on the right.
   The map remains a single mounted instance to avoid reinitialization errors. */
.asl-delivery-modal__main {min-width:0}
.asl-delivery-modal__left {min-width:0}
@media screen and (min-width: 990px) {
  #AslDeliveryModal-{{ section.id }}.asl-delivery-modal--boxnow .asl-delivery-modal__panel {
    width: min(1080px, calc(100vw - 48px)) !important;
    max-width: calc(100vw - 48px) !important;
  }
  #AslDeliveryModal-{{ section.id }}.asl-delivery-modal--boxnow .asl-delivery-modal__main {
    display: grid;
    grid-template-columns: minmax(270px, .75fr) minmax(0, 1.25fr);
    gap: clamp(20px, 3vw, 42px);
    align-items: start;
    margin-top: 16px;
  }
  #AslDeliveryModal-{{ section.id }}.asl-delivery-modal--boxnow .asl-delivery-modal__options {
    margin: 0;
  }
  #AslDeliveryModal-{{ section.id }}.asl-delivery-modal--boxnow .asl-delivery-modal__boxnow {
    min-width: 0;
    border-top: 0;
    border-left: 1px solid var(--adl-border);
    padding: 0 0 10px clamp(18px, 2vw, 32px);
  }
  #AslDeliveryModal-{{ section.id }}.asl-delivery-modal--boxnow .asl-boxnow-map-slot {
    width: 100%;
    min-width: 0;
  }
}
@media (max-width: 989px) {
  .asl-delivery-modal__main {display:block}
}
/* v11 — Keep the BOX NOW desktop popup a constant size. The *whole* popup,
   including its Continue button, scrolls in one scroll container. */
@media screen and (min-width: 990px) {
  #AslDeliveryModal-{{ section.id }}.asl-delivery-modal--boxnow .asl-delivery-modal__panel {
    height: min(700px, calc(100dvh - var(--adl-header-offset, 0px) - 32px)) !important;
    max-height: calc(100dvh - var(--adl-header-offset, 0px) - 32px) !important;
    overflow-y: auto !important;
    overflow-x: hidden !important;
    overscroll-behavior: contain;
    scrollbar-gutter: stable;
    scroll-behavior: smooth;
  }
  /* The action follows the map in normal document flow: no sticky footer. */
  #AslDeliveryModal-{{ section.id }} .asl-delivery-modal__continue {
    position: static !important;
    margin-top: 18px;
  }
  #AslDeliveryModal-{{ section.id }} .asl-delivery-modal__boxnow {
    scroll-margin-top: 22px;
  }
}
@media (prefers-reduced-motion: reduce) {
  #AslDeliveryModal-{{ section.id }} .asl-delivery-modal__panel {scroll-behavior:auto !important}
}

/* ACS Smartpoint selector — desktop follows the right-column BOX NOW pattern. */
.asl-delivery-modal__acs{min-width:0;border-top:1px solid var(--adl-border);padding:16px 0 20px}
.asl-delivery-modal__acs h3{font-size:17px;margin:0 0 8px}
.asl-acs-label{display:block;font-size:13px;margin:12px 0 6px}
.asl-acs-search{box-sizing:border-box;width:100%;font:inherit;font-size:14px;min-height:45px;border:1px solid var(--adl-border);border-radius:var(--adl-radius);background:var(--adl-bg);color:var(--adl-text);padding:10px 12px}
.asl-acs-status{font-size:12px;color:var(--adl-muted);margin:10px 0}
.asl-acs-results{display:grid;gap:8px;max-height:330px;overflow:auto;overscroll-behavior:contain}
.asl-acs-result{font:inherit;text-align:left;display:flex;justify-content:space-between;gap:12px;align-items:start;width:100%;border:1px solid var(--adl-border);border-radius:8px;background:var(--adl-bg);color:var(--adl-text);padding:12px;cursor:pointer}
.asl-acs-result:hover,.asl-acs-result:focus-visible,.asl-acs-result[aria-pressed="true"]{border-color:var(--adl-accent);outline:1px solid var(--adl-accent)}
.asl-acs-result strong{display:block;font-size:13px}.asl-acs-result small{display:block;font-size:12px;color:var(--adl-muted);margin-top:4px}
.asl-acs-selected{margin-top:12px;border:1px solid var(--adl-accent);padding:12px;border-radius:8px;font-size:13px}
#AslDeliveryModal-{{ section.id }}.asl-delivery-modal--acs .asl-delivery-modal__continue{margin-top:18px}
@media(min-width:990px){
 #AslDeliveryModal-{{ section.id }}.asl-delivery-modal--acs .asl-delivery-modal__panel{width:min(1080px,calc(100vw - 48px))!important;height:min(700px,calc(100dvh - var(--adl-header-offset,0px) - 32px))!important;max-height:calc(100dvh - var(--adl-header-offset,0px) - 32px)!important;overflow-y:auto!important;overflow-x:hidden!important;scrollbar-gutter:stable}
 #AslDeliveryModal-{{ section.id }}.asl-delivery-modal--acs .asl-delivery-modal__main{display:grid;grid-template-columns:minmax(270px,.75fr) minmax(0,1.25fr);gap:clamp(20px,3vw,42px);align-items:start;margin-top:16px}
 #AslDeliveryModal-{{ section.id }}.asl-delivery-modal--acs .asl-delivery-modal__options{margin:0}
 #AslDeliveryModal-{{ section.id }}.asl-delivery-modal--acs .asl-delivery-modal__acs{border-top:0;border-left:1px solid var(--adl-border);padding:0 0 10px clamp(18px,2vw,32px);scroll-margin-top:22px}
}
</style>
<script>
(() => {
  const id = {{ section.id | json }};
  const modal = document.getElementById('AslDeliveryModal-' + id);
  if (!modal || modal.dataset.ready) return;
  modal.dataset.ready = '1';
  const panel = modal.querySelector('.asl-delivery-modal__panel');
  // Keep the entire delivery dialog beneath the visible header/announcement bars.
  // Only count top-of-viewport header elements; avoid treating other page sections as headers.
  const updateDeliveryHeaderOffset = () => {
    const selectors = [
      '#shopify-section-announcement-bar',
      '.announcement-bar-section',
      '.shopify-section-group-header-group',
      '.section-header',
      'sticky-header',
      '#shopify-section-header',
      'header.header'
    ];
    let edge = 0;
    const maxHeaderHeight = window.innerHeight * 0.45;
    const seen = new Set();
    selectors.forEach(selector => document.querySelectorAll(selector).forEach(el => {
      if (seen.has(el) || modal.contains(el)) return;
      seen.add(el);
      const rect = el.getBoundingClientRect();
      const style = window.getComputedStyle(el);
      if (style.display === 'none' || style.visibility === 'hidden') return;
      // The element must currently intersect the top of the viewport.
      if (rect.top <= 5 && rect.bottom > 0 && rect.bottom <= maxHeaderHeight) {
        edge = Math.max(edge, rect.bottom);
      }
    }));
    modal.style.setProperty('--adl-header-offset', Math.ceil(edge) + 'px');
  };
  const refreshDeliveryHeaderOffset = () => {
    if (!modal.hidden) updateDeliveryHeaderOffset();
  };
  window.addEventListener('resize', refreshDeliveryHeaderOffset, {passive:true});
  window.addEventListener('orientationchange', refreshDeliveryHeaderOffset);
  window.addEventListener('scroll', refreshDeliveryHeaderOffset, {passive:true});

  const errors = modal.querySelector('[data-delivery-error]');
  const continueButton = modal.querySelector('[data-delivery-continue]');
  const boxArea = modal.querySelector('[data-boxnow-area]');
  const acsArea = modal.querySelector('[data-acs-area]');
  const acsSearch = modal.querySelector('[data-acs-search]');
  const acsResults = modal.querySelector('[data-acs-results]');
  const acsStatus = modal.querySelector('[data-acs-status]');
  const acsSelected = modal.querySelector('[data-acs-selected]');
  const acsFeedUrl = {{ section.settings.delivery_acs_json_url | json }}.trim();
  let acsPoints = [], selectedAcs = null, acsLoaded = false;
  const acsFields = p => {
    // Native ACS_Stations and normalized JSON feeds are supported.
    const val = (...items) => items.find(v => v !== undefined && v !== null && String(v).trim() !== '') ?? '';
    const countryValue = String(val(p.ACS_SHOP_COUNTRY_ID, p.ACS_SHOP_COUNTRY_DESCR,
      p.country_code, p.countryCode, p.country, p.Country, p.CountryCode, p.Country_Code)).trim();
    const country = countryValue.toUpperCase();
    // ACS calls Greece GR (or 1 in some response variants). Do not guess
    // locations from a Greek-looking postcode if country is absent.
    const isGreece = ['GR', 'GRC', 'GREECE', 'ΕΛΛΑΔΑ', 'ΕΛΛΑΣ', '1'].includes(country);
    const kind = String(val(p.ACS_SHOP_KIND, p.shop_kind, p.shopKind, p.kind)).trim();
    // ACS 8 = Smartpoint parcel locker; 12 = parcel lockers outside stores.
    // 7 is a pickup smartpoint without a locker and must be excluded.
    const type = String(val(p.type, p.Type, p.Station_Type, p.StationType, p.station_type)).trim();
    // The GitHub ACS_Get_Stations_For_Plugin feed includes ordinary ACS
    // points too. Never classify every point as a parcel locker.
    const lockerFlag = p.is_locker === true || p.isLocker === true ||
      String(p.is_locker ?? p.isLocker ?? '').toLowerCase() === 'true';
    const lockerType = /locker|θυριδ|lockers|αυτόματο.*παραλαβ/i.test(type);
    const locker = kind ? ['8','12'].includes(kind) : (lockerFlag || lockerType);
    const station = String(val(p.station_code, p.Acs_Station_Destination,
      p.ACS_SHOP_STATION_ID, p.Station_Code, p.StationCode, p.stationCode)).trim();
    const branch = String(val(p.branch_code, p.Acs_Station_Branch_Destination,
      p.ACS_SHOP_BRANCH_ID, p.Branch_Code, p.BranchCode, p.branchCode)).trim();
    const code = String(val(p.code,p.Code,p.ACS_SHOP_ID_CODE,p.ID,p.id,
      station && branch ? station + '-' + branch : station)).trim();
    // Preserve a real venue/shop name if the feed supplies one; never infer a
    // host business from the locker ID or generic ACS station description.
    const venue = String(val(p.venue_name,p.venueName,p.Venue_Name,p.VENUE_NAME,
      p.host_store_name,p.hostStoreName,p.Host_Store_Name,p.store_name,p.storeName,
      p.Store_Name,p.STORE_NAME,p.shop_name,p.shopName,p.Shop_Name,
      p.ACS_SHOP_NAME,p.ACS_SHOP_DESCR,p.ACS_SHOP_TITLE,
      p.business_name,p.businessName,p.Business_Name,p.location_name,
      p.locationName,p.Location_Name,p.point_name,p.Point_Name)).trim();
    const rawName = String(val(p.name,p.Name,p.ACS_SHOP_STATION_DESCR,
      p.Acs_Station_Description,p.Description,p.description,p.Station_Name)).trim();
    const city = String(val(p.city,p.City,p.ACS_SHOP_AREA_DESCR,p.Acs_Station_City,p.Town,p.Area)).trim();
    const postcode = String(val(p.postcode,p.postal_code,p.ACS_SHOP_ZIPCODE,
      p.ZipCode,p.PostalCode,p.Zip_Code,p.ZIP)).trim();
    const street = String(val(p.address,p.Address,p.ACS_SHOP_ADDRESS,p.Acs_Station_Address,
      p.ACS_SHOP_STREET,p.ACS_SHOP_ADDRESS1,p.address_line_1,p.address1,
      p.street_address,p.streetAddress,p.Street,p.street)).trim();
    const number = String(val(p.street_number,p.streetNumber,p.Street_Number,p.ACS_SHOP_STREET_NO)).trim();
    const address = street && number && !street.includes(number) ? street + ' ' + number : street;
    const genericName = /^(?:acs[\s_-]*)?(?:smart[\s_-]*point|locker|parcel[\s_-]*locker)(?:[\s_-]*(?:locker|point))?(?:\s*[-–—]\s*.+)?$/i.test(rawName) ||
      /^ACS\s+SMARTPOINT\s+LOCKER/i.test(rawName);
    const name = venue || (rawName && !genericName ? rawName :
      `ACS Locker${city ? ' — ' + city : ''}`);
    return { code,name,venue,address,city,postcode,station,branch,search_aliases:String(p.search_aliases || p.aliases || ''),isGreece,isLocker:locker };
  };
  const acsMessage = message => { acsStatus.textContent = message; };
  const selectAcs = p => {
    selectedAcs = p;
    acsSelected.hidden = false;
    acsSelected.textContent = `Επιλέχθηκε: ${p.name}${p.address ? ' — ' + p.address : ''}${p.city ? ', ' + p.city : ''}${p.postcode ? ' ' + p.postcode : ''} (${p.code})`;
    acsResults.querySelectorAll('button').forEach(b => b.setAttribute('aria-pressed',String(b.dataset.code === p.code)));
  };
  // Search Greek, unaccented Greek, and Latin/Greeklish in both directions.
  const greekLetters = {'α':'a','β':'v','γ':'g','δ':'d','ε':'e','ζ':'z','η':'i','θ':'th','ι':'i','κ':'k','λ':'l','μ':'m','ν':'n','ξ':'x','ο':'o','π':'p','ρ':'r','σ':'s','ς':'s','τ':'t','υ':'u','φ':'f','χ':'ch','ψ':'ps','ω':'o'};
  const unaccented = text => String(text ?? '').normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase().replace(/ς/g,'σ');
  const toLatin = text => [...unaccented(text)].map(c => greekLetters[c] ?? c).join('')
    .replace(/ou/g,'u').replace(/ai/g,'e').replace(/ei/g,'i').replace(/oi/g,'i');
  const normalizeSearch = text => toLatin(text).replace(/[^a-z0-9]+/g,' ').trim();
  const aliases = {
    'athens':['athina','athinas','athina','athens','athin'],
    'athina':['athens','athina','athin'],
    'thessaloniki':['thessaloniki','thesaloniki','saloniki','salonica','salonika'],
    'saloniki':['thessaloniki','thesaloniki','salonica'],
    'patras':['patra','patras'], 'patra':['patras'],
    'heraklion':['iraklio','irakleio','heraklion','heraklio'],
    'iraklio':['heraklion','irakleio'],
    'chania':['hania','chania','chanya'],
    'rhodes':['rodos','rhodes','rodos'], 'rodos':['rhodes'],
    'corfu':['kerkyra','corfu','kerkira'], 'kerkyra':['corfu','kerkira'],
    'kos':['kos','cos'], 'ioannina':['ioannina','giannena','yiannena'],
    'larissa':['larisa','larissa'], 'volos':['volos'],
    'chios':['hios','chios'], 'kavala':['kavala'],
    'zakynthos':['zakynthos','zante'], 'lesvos':['lesvos','mytilini','mitilini']
  };
  const searchForms = text => {
    const original = normalizeSearch(text);
    const forms = new Set([original, original.replace(/\s/g,'')]);
    Object.entries(aliases).forEach(([key,options]) => {
      if (key===original || options.includes(original)) { forms.add(key);options.forEach(v=>forms.add(v)); }
    });
    // Alternative common digraph spellings (e.g. thessaloniki/thesaloniki).
    [...forms].forEach(v => {forms.add(v.replace(/th/g,'8').replace(/ch/g,'h').replace(/ou/g,'u'));});
    return [...forms].filter(Boolean);
  };
  const isMatch = (p,query) => {
    const haystack = normalizeSearch([p.name,p.venue,p.address,p.city,p.postcode,p.code,p.search_aliases||''].join(' '));
    const simple = haystack.replace(/\s/g,'');
    const words = query.trim().split(/\s+/).filter(Boolean);
    return words.every(word => searchForms(word).some(form => haystack.includes(form) || simple.includes(form)));
  };
  const drawAcs = () => {
    acsResults.replaceChildren();
    const search = acsSearch.value.trim();
    const visible = search ? acsPoints.filter(p => isMatch(p,search)) : acsPoints;
    acsMessage(`${visible.length} από ${acsPoints.length} ACS lockers στην Ελλάδα` + (search && !visible.length ? ' — δοκιμάστε ελληνικά, Greeklish, αγγλικά ή κωδικό locker. Αναζήτηση ΤΚ μόνο όπου υπάρχει ΤΚ στο αρχείο.' : ''));
    const fragment = document.createDocumentFragment();
    visible.forEach(p => {
      const b=document.createElement('button'); b.type='button'; b.className='asl-acs-result';
      b.dataset.code=p.code; b.setAttribute('aria-pressed',String(selectedAcs?.code===p.code));
      const info=document.createElement('span'), title=document.createElement('strong'), address=document.createElement('small'), idSpan=document.createElement('small');
      title.textContent=p.name;
      address.textContent=[p.address,p.city,p.postcode].filter(Boolean).join(' · ') || 'Η ACS δεν δημοσιεύει πλήρη διεύθυνση σε αυτή την πηγή';
      idSpan.textContent=p.code;
      info.append(title,address); b.append(info,idSpan);
      b.addEventListener('click',()=>selectAcs(p)); fragment.appendChild(b);
    });
    acsResults.appendChild(fragment);
  };
  const loadAcs = async () => {
    if (acsLoaded) return;
    if (!acsFeedUrl) { acsMessage('Ορίστε ACS JSON URL από τις ρυθμίσεις του Theme Editor.'); return; }
    acsMessage('Φόρτωση ACS lockers…');
    try {
      const response = await fetch(acsFeedUrl,{mode:'cors'});
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const raw = await response.json();
      const rows = Array.isArray(raw) ? raw :
        (raw.ACSOutputResponse?.ACSTableOutput?.Table_Data1 ??
         raw.ACSOutputResponce?.ACSTableOutput?.Table_Data1 ??
         raw.ACSOutputResponse?.ACSTableOutput?.Table_Data ??
         raw.ACSOutputResponce?.ACSTableOutput?.Table_Data ??
         raw.stations ?? raw.points ?? raw.data ?? raw.Stations ?? raw.result ?? []);
      if (!Array.isArray(rows)) throw new Error('Expected an array of ACS stations');
      const all = rows.map(acsFields);
      acsPoints = all.filter(p => p.isGreece && p.isLocker && p.code && p.name)
        .sort((a,b) => a.city.localeCompare(b.city,'el') || a.name.localeCompare(b.name,'el'));
      acsLoaded = true;
      drawAcs();
      if (!acsPoints.length) {
        const greek = all.filter(p => p.isGreece);
        const lockers = greek.filter(p => p.isLocker);
        if (!rows.length) acsMessage('Το ACS JSON δεν περιέχει σημεία. Ελέγξτε την πηγή δεδομένων.');
        else if (!greek.length) acsMessage(`Το JSON περιέχει ${rows.length} σημεία αλλά κανένα με αναγνωρίσιμη χώρα Ελλάδα (Country_Code: GR).`);
        else if (!lockers.length) acsMessage(`Βρέθηκαν ${greek.length} σημεία ACS στην Ελλάδα, αλλά η πηγή δεν προσδιορίζει ποια είναι lockers. Χρειάζεται ACS_SHOP_KIND 8/12 ή is_locker=true. Δεν θα εμφανιστούν τυχαία καταστήματα ως lockers.`);
        else acsMessage(`Βρέθηκαν ${lockers.length} lockers στην Ελλάδα, αλλά λείπουν τα αναγνωριστικά ή τα ονόματά τους.`);
      }
    } catch(ex) { acsMessage(`Αδυναμία φόρτωσης ACS: ${ex.message}`); }
  };
  acsSearch.addEventListener('input',drawAcs);
  const showAcs = () => {acsArea.hidden=false;loadAcs();if(window.innerWidth>=990)requestAnimationFrame(()=>acsArea.scrollIntoView({block:'nearest',behavior:'smooth'}));};

  const boxMount = modal.querySelector('[data-boxnow-mount]');
  const boxMissing = modal.querySelector('[data-boxnow-missing]');
  const labels = {
    required: {{ section.settings.delivery_required_error | json }},
    saving: {{ section.settings.delivery_saving_text | json }},
    continue: {{ section.settings.delivery_continue_text | json }},
    saveError: {{ section.settings.delivery_save_error | json }}
  };
  let movedBoxBlock = null;
  let mountRetry = null;
  let sourceObserver = null;
  const refreshMapLayout = () => requestAnimationFrame(() => {
    window.dispatchEvent(new Event('resize'));
    setTimeout(() => window.dispatchEvent(new Event('resize')), 180);
  });
  const BOX_NOW_APP_BLOCK_SELECTOR = {{ section.settings.delivery_app_selector | json }}.trim();
  const findBoxNowBlock = () => {
    if (BOX_NOW_APP_BLOCK_SELECTOR) {
      try { const exact = document.querySelector(BOX_NOW_APP_BLOCK_SELECTOR); if (exact && !modal.contains(exact)) return exact; }
      catch(err) { console.warn('Invalid BOX NOW selector',err); }
    }
    const signatureMatches = el => {
      if (modal.contains(el)) return false;
      const signature = [el.id || '', typeof el.className === 'string' ? el.className : '',
        ...Array.from(el.querySelectorAll('iframe[src]')).map(f => f.src)].join(' ').toLowerCase();
      return /box.?now/.test(signature);
    };
    const appBlocks = Array.from(document.querySelectorAll('.shopify-app-block, [id^="shopify-block-"]'));
    const found = appBlocks.find(signatureMatches);
    if (found) return found;
    return Array.from(document.querySelectorAll('.shopify-section')).find(el =>
      !el.contains(document.getElementById('main-cart-footer')) && signatureMatches(el)
    ) || null;
  };
  const concealSource = () => {
    if (movedBoxBlock) return true;
    const el = findBoxNowBlock();
    if (!el) return false;
    el.classList.add('asl-boxnow-prelaunch');
    const parentSection = el.closest('.shopify-section');
    if (parentSection && parentSection !== document.getElementById('main-cart-footer')?.closest('.shopify-section')
      && (el === parentSection || parentSection.querySelectorAll('.shopify-app-block').length === 1)) {
      parentSection.classList.add('asl-boxnow-prelaunch-section');
    }
    return true;
  };
  const watchSource = () => {
    if (concealSource()) return;
    sourceObserver = new MutationObserver(() => {
      if (concealSource()) { sourceObserver.disconnect(); sourceObserver = null; }
    });
    sourceObserver.observe(document.body, {childList:true,subtree:true});
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', watchSource, {once:true});
  else watchSource();
  const attachBoxNow = () => {
    if (movedBoxBlock && movedBoxBlock.isConnected) {boxMissing.hidden = true;refreshMapLayout();return true;}
    const element = findBoxNowBlock();
    if (!element) {boxMissing.hidden = false;return false;}
    boxMissing.hidden = true;
    movedBoxBlock = element;
    if (sourceObserver) {sourceObserver.disconnect();sourceObserver = null;}
    boxMount.appendChild(element);
    element.classList.remove('asl-boxnow-prelaunch');
    refreshMapLayout();
    return true;
  };
  // Scroll only the popup's content, never the cart page behind it.
  const scrollToLockerWidget = () => {
    if (window.innerWidth < 990 || modal.hidden || method() !== 'boxnow') return;
    requestAnimationFrame(() => requestAnimationFrame(() => {
      const panelRect = panel.getBoundingClientRect();
      const areaRect = boxArea.getBoundingClientRect();
      const desired = panel.scrollTop + areaRect.top - panelRect.top - 22;
      panel.scrollTo({top: Math.max(0, desired), behavior:
        window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth'});
    }));
  };
  const showBoxNow = () => {
    boxArea.hidden = false;
    if (!attachBoxNow()) {
      clearTimeout(mountRetry);
      mountRetry = setTimeout(() => {
        if (!modal.hidden && method() === 'boxnow') {
          attachBoxNow();
          scrollToLockerWidget();
        }
      },500);
    }
    scrollToLockerWidget();
  };
  const shopifyCartUpdateUrl = {{ routes.cart_update_url | append: '.js' | json }};
  const shopifyCartUrl = {{ routes.cart_url | append: '.js' | json }};
  let checkoutSubmitter = null;
  let bypass = false;
  let focusReturn = null;
  const cartForm = document.getElementById('cart');
  const error = (message) => {errors.textContent = message;errors.hidden = !message;};
  const syncDeliveryLayout = () => { modal.classList.toggle('asl-delivery-modal--boxnow', method() === 'boxnow'); modal.classList.toggle('asl-delivery-modal--acs', method() === 'acs'); };
  const method = () => modal.querySelector('input[name="asl-delivery-method-' + id + '"]:checked')?.value;
  const show = submitter => {
    checkoutSubmitter = submitter || document.getElementById('checkout');
    focusReturn = document.activeElement;
    error('');
    updateDeliveryHeaderOffset();
    modal.hidden = false;
    modal.setAttribute('aria-hidden','false');
    document.body.classList.add('asl-delivery-modal-open');
    panel.focus();
    requestAnimationFrame(updateDeliveryHeaderOffset);
    syncDeliveryLayout();
    if (method() === 'boxnow') showBoxNow();
    if (method() === 'acs') showAcs();
  };
  const hide = () => {
    modal.hidden = true;
    modal.setAttribute('aria-hidden','true');
    document.body.classList.remove('asl-delivery-modal-open');
    focusReturn?.focus?.();
  };
  modal.querySelectorAll('[data-delivery-close]').forEach(el => el.addEventListener('click',hide));
  modal.querySelectorAll('input[type="radio"]').forEach(input => input.addEventListener('change',() => {
    boxArea.hidden = method() !== 'boxnow';
    acsArea.hidden = method() !== 'acs';
    syncDeliveryLayout();
    if (method() === 'boxnow') showBoxNow();
    if (method() === 'acs') showAcs();
    else panel.scrollTo({top: 0, behavior: 'instant'});
    error('');
  }));
  modal.addEventListener('keydown',e => {
    if (e.key === 'Escape'){e.preventDefault();hide();}
    if (e.key === 'Tab'){
      const els = [...panel.querySelectorAll('button:not([disabled]),input:not([disabled]):not([hidden])')].filter(x => x.getClientRects().length);
      if (!els.length) return;
      if (e.shiftKey && document.activeElement === els[0]){e.preventDefault();els.at(-1).focus();}
      else if (!e.shiftKey && document.activeElement === els.at(-1)){e.preventDefault();els[0].focus();}
    }
  });
  document.addEventListener('click',e => {
    const button = e.target.closest?.('#main-cart-footer #checkout, #main-cart-footer #checkout-klarna');
    if (!button || bypass || button.disabled) return;
    e.preventDefault();e.stopPropagation();e.stopImmediatePropagation();show(button);
  },true);
  cartForm?.addEventListener('submit',e => {
    if (bypass || e.submitter?.id === 'CartDrawer-Checkout') return;
    if (e.submitter?.name === 'checkout' || !e.submitter){
      e.preventDefault();e.stopImmediatePropagation();show(e.submitter);
    }
  },true);
  const getCart = async () => {
    const response = await fetch(shopifyCartUrl,{credentials:'same-origin',headers:{Accept:'application/json'}});
    if (!response.ok) throw new Error(labels.saveError);
    return response.json();
  };
  const save = async selected => {
    const oldCart = await getCart();
    // Keep app-owned locker attributes untouched. Only the method is controlled here.
    const attributes = {...oldCart.attributes,'Delivery Method':selected === 'boxnow' ? 'BOX NOW Locker' : selected === 'acs' ? 'ACS Smartpoint Locker' : 'Courier'};
    delete attributes['Delivery Locker Confirmation'];
    // Remove stale ACS selection whenever another delivery method is chosen.
    const fields=['ACS Locker ID','ACS Locker Name','ACS Locker Venue','ACS Locker Address','ACS Locker City','ACS Locker Postcode','ACS Station Destination','ACS Station Branch Destination'];
    fields.forEach(k => {attributes[k] = selected==='acs' ? ({
      'ACS Locker ID': selectedAcs?.code,'ACS Locker Name':selectedAcs?.name,
      'ACS Locker Venue':selectedAcs?.venue,
      'ACS Locker Address':selectedAcs?.address,'ACS Locker City':selectedAcs?.city,
      'ACS Locker Postcode':selectedAcs?.postcode,
      'ACS Station Destination':selectedAcs?.station,
      'ACS Station Branch Destination':selectedAcs?.branch
    }[k] ?? '') : '';});
    const response = await fetch(shopifyCartUpdateUrl,{
      method:'POST',credentials:'same-origin',headers:{'Content-Type':'application/json',Accept:'application/json'},
      body:JSON.stringify({attributes})
    });
    if (!response.ok) throw new Error(labels.saveError);
    const result = await response.json();
    if (result.attributes?.['Delivery Method'] !== attributes['Delivery Method']) throw new Error(labels.saveError);
  };
  continueButton.addEventListener('click',async () => {
    const selected = method();
    if (!selected) return error(labels.required);
    if (selected === 'boxnow' && !movedBoxBlock) return error(boxMissing.textContent.trim());
    if (selected === 'acs' && !selectedAcs) return error('Επιλέξτε πρώτα ένα ACS Smartpoint Locker.');
    // The BOX NOW app owns locker choice and validation; no duplicate confirmation checkbox.
    error('');continueButton.disabled=true;continueButton.textContent=labels.saving;
    try {
      await save(selected);
      bypass=true;
      hide();
      if (cartForm && checkoutSubmitter && cartForm.requestSubmit){cartForm.requestSubmit(checkoutSubmitter);}
      else {window.location.assign({{ routes.root_url | append: 'checkout' | json }});}
    } catch(ex){bypass=false;error(ex.message || labels.saveError);}
    finally{continueButton.disabled=false;continueButton.textContent=labels.continue;}
  });
})();
</script>

{%- if gift_bag_count > 0 -%}
  <div
    class="asl-giftwrap-modal"
    id="AslGiftWrapModal-{{ section.id }}"
    aria-hidden="true"
  >
    <div class="asl-giftwrap-modal__overlay" data-asl-gift-close></div>

    <div
      class="asl-giftwrap-modal__panel"
      role="dialog"
      aria-modal="true"
      aria-labelledby="AslGiftWrapTitle-{{ section.id }}"
    >
      <button
        type="button"
        class="asl-giftwrap-modal__close"
        data-asl-gift-close
        aria-label="Κλείσιμο"
      >
        ×
      </button>

      <div class="asl-giftwrap-modal__inner">
        <h2
          class="asl-giftwrap-modal__title"
          id="AslGiftWrapTitle-{{ section.id }}"
        >
          {{ section.settings.gift_wrap_title }}
        </h2>

        {%- if section.settings.gift_wrap_description != blank -%}
          <div class="asl-giftwrap-modal__description rte">
            {{ section.settings.gift_wrap_description }}
          </div>
        {%- endif -%}

        <div class="asl-giftwrap-modal__variants">
          {%- for block in section.blocks -%}
            {%- if block.type == 'gift_bag_small' or block.type == 'gift_bag_medium' -%}
              {%- assign bag_product = block.settings.product -%}

              {%- if bag_product != blank -%}
                {%- assign bag_variant = bag_product.selected_or_first_available_variant -%}

                <div
                  class="asl-giftwrap-variant"
                  data-variant-id="{{ bag_variant.id }}"
                  data-variant-price="{{ bag_variant.price }}"
                  {{ block.shopify_attributes }}
                >
                  <div class="asl-giftwrap-variant__info">
                    {%- if bag_product.featured_image != blank -%}
                      {{
                        bag_product.featured_image
                        | image_url: width: 160
                        | image_tag:
                          class: 'asl-giftwrap-variant__thumb',
                          loading: 'lazy',
                          alt: bag_product.title
                      }}
                    {%- endif -%}

                    <div class="asl-giftwrap-variant__text">
                      <span class="asl-giftwrap-variant__name">
                        {%- if block.settings.label != blank -%}
                          {{ block.settings.label }}
                        {%- elsif block.type == 'gift_bag_small' -%}
                          Μικρό
                        {%- else -%}
                          Μεσαίο
                        {%- endif -%}
                      </span>

                      <span class="asl-giftwrap-variant__price">
                        {{ bag_variant.price | money }}
                      </span>
                    </div>
                  </div>

                  <div class="asl-giftwrap-qty">
                    <button
                      type="button"
                      class="asl-giftwrap-qty__button"
                      data-action="minus"
                      aria-label="Μείωση ποσότητας"
                    >−</button>

                    <input
                      class="asl-giftwrap-qty__input"
                      type="number"
                      value="0"
                      min="0"
                      readonly
                      aria-label="Ποσότητα συσκευασίας δώρου"
                    >

                    <button
                      type="button"
                      class="asl-giftwrap-qty__button"
                      data-action="plus"
                      aria-label="Αύξηση ποσότητας"
                    >+</button>
                  </div>
                </div>
              {%- endif -%}
            {%- endif -%}
          {%- endfor -%}
        </div>

        {%- if section.settings.gift_wrap_image != blank -%}
          <div class="asl-giftwrap-modal__hero">
            {{
              section.settings.gift_wrap_image
              | image_url: width: 1400
              | image_tag:
                loading: 'lazy',
                alt: section.settings.gift_wrap_title
            }}
          </div>
        {%- endif -%}

        <div class="asl-giftwrap-modal__footer">
          <div class="asl-giftwrap-modal__total">
            <span>ΣΥΝΟΛΟ:</span>
            <strong data-asl-gift-total>{{ 0 | money }}</strong>
          </div>

          <button
            type="button"
            class="asl-giftwrap-modal__add"
            data-asl-gift-add
            disabled
          >
            {{ section.settings.gift_wrap_add_text }}
          </button>
        </div>
      </div>
    </div>
  </div>

  <script>
    (() => {
      const sectionId = {{ section.id | json }};
      const modal = document.getElementById(`AslGiftWrapModal-${sectionId}`);
      const openButton = document.getElementById(`AslGiftWrapOpen-${sectionId}`);

      if (!modal || !openButton || modal.dataset.aslReady === 'true') return;
      modal.dataset.aslReady = 'true';

      const rows = Array.from(modal.querySelectorAll('.asl-giftwrap-variant'));
      const addButton = modal.querySelector('[data-asl-gift-add]');
      const totalElement = modal.querySelector('[data-asl-gift-total]');
      const normalAddText = {{ section.settings.gift_wrap_add_text | json }};
      const loadingText = {{ section.settings.gift_wrap_loading_text | json }};
      const currency = {{ cart.currency.iso_code | json }};
      const locale = {{ request.locale.iso_code | json }};

      /* ---------------------------------------------------------
         Keep the gift bag drawer below the announcement + header.
         We calculate the lowest visible header edge instead of using
         a hard-coded pixel value, so it also works when header height,
         announcement bars, language selectors, or sticky header state change.
      --------------------------------------------------------- */
      const getGiftWrapHeaderOffset = () => {
        const selectors = [
          '.shopify-section-group-header-group',
          '#shopify-section-announcement-bar',
          '.announcement-bar-section',
          '.section-header',
          'sticky-header',
          'header.header'
        ];

        let bottom = 0;

        selectors.forEach((selector) => {
          document.querySelectorAll(selector).forEach((element) => {
            const rect = element.getBoundingClientRect();

            /* Only count elements that are actually intersecting the
               top/visible portion of the viewport. */
            if (
              rect.height > 0 &&
              rect.bottom > 0 &&
              rect.top < window.innerHeight
            ) {
              bottom = Math.max(bottom, rect.bottom);
            }
          });
        });

        return Math.max(
          0,
          Math.min(window.innerHeight, Math.round(bottom))
        );
      };

      const setGiftWrapHeaderOffset = () => {
        document.documentElement.style.setProperty(
          '--asl-giftwrap-header-offset',
          `${getGiftWrapHeaderOffset()}px`
        );
      };

      const formatMoney = (cents) => {
        try {
          return new Intl.NumberFormat(locale, {
            style: 'currency',
            currency: currency
          }).format(cents / 100);
        } catch (error) {
          return (cents / 100).toFixed(2) + ' ' + currency;
        }
      };

      const calculateTotal = () => {
        let total = 0;
        let quantity = 0;

        rows.forEach((row) => {
          const input = row.querySelector('.asl-giftwrap-qty__input');
          const qty = Math.max(0, Number(input?.value || 0));
          const price = Number(row.dataset.variantPrice || 0);

          total += price * qty;
          quantity += qty;
        });

        totalElement.textContent = formatMoney(total);
        addButton.disabled = quantity === 0;
      };

      const openModal = () => {
        /* Calculate BEFORE showing the drawer so it never flashes over
           the announcement bar/header. Recalculate once more next frame
           in case a sticky header changed state. */
        setGiftWrapHeaderOffset();

        modal.classList.add('is-open');
        modal.setAttribute('aria-hidden', 'false');
        document.body.classList.add('asl-giftwrap-open');

        requestAnimationFrame(setGiftWrapHeaderOffset);
      };

      const closeModal = () => {
        modal.classList.remove('is-open');
        modal.setAttribute('aria-hidden', 'true');
        document.body.classList.remove('asl-giftwrap-open');
      };

      rows.forEach((row) => {
        const input = row.querySelector('.asl-giftwrap-qty__input');
        const minus = row.querySelector('[data-action="minus"]');
        const plus = row.querySelector('[data-action="plus"]');

        minus?.addEventListener('click', () => {
          input.value = Math.max(0, Number(input.value || 0) - 1);
          calculateTotal();
        });

        plus?.addEventListener('click', () => {
          input.value = Number(input.value || 0) + 1;
          calculateTotal();
        });
      });

      openButton.addEventListener('click', openModal);

      modal.querySelectorAll('[data-asl-gift-close]').forEach((element) => {
        element.addEventListener('click', closeModal);
      });

      document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape' && modal.classList.contains('is-open')) {
          closeModal();
        }
      });

      addButton.addEventListener('click', async (event) => {
        event.preventDefault();

        const items = [];

        rows.forEach((row) => {
          const input = row.querySelector('.asl-giftwrap-qty__input');
          const quantity = Math.max(0, parseInt(input?.value || '0', 10));
          const variantId = parseInt(row.dataset.variantId || '0', 10);

          if (quantity > 0 && Number.isFinite(variantId) && variantId > 0) {
            items.push({
              id: variantId,
              quantity: quantity
            });
          }
        });

        if (!items.length) {
          calculateTotal();
          return;
        }

        addButton.disabled = true;
        addButton.textContent = loadingText;

        try {
          /*
            Use Shopify's actual cart-add route from Liquid rather than
            constructing the URL in JavaScript. This is safer for stores
            using locale/subfolder routes and reliably supports multiple items.
          */
          /*
            Shopify AJAX Cart API MUST use the .js endpoint.
            routes.cart_add_url is normally /cart/add (HTML/form endpoint),
            so append .js for a proper JSON AJAX response.
          */
          const cartAddUrl = {{ routes.cart_add_url | append: '.js' | json }};

          const response = await fetch(cartAddUrl, {
            method: 'POST',
            credentials: 'same-origin',
            headers: {
              'Content-Type': 'application/json',
              'Accept': 'application/json',
              'X-Requested-With': 'XMLHttpRequest'
            },
            body: JSON.stringify({
              items: items
            })
          });

          const responseText = await response.text();

          let result = {};
          try {
            result = responseText ? JSON.parse(responseText) : {};
          } catch (parseError) {
            result = {};
          }

          if (!response.ok) {
            const message =
              result?.description ||
              result?.message ||
              result?.status ||
              responseText ||
              `Shopify rejected the gift bag request (${response.status}).`;

            throw new Error(message);
          }

          /*
            Verify the cart was actually updated before refreshing.
            This avoids a silent reload when Shopify rejected an item.
          */
          const cartResponse = await fetch({{ routes.cart_url | append: '.js' | json }}, {
            method: 'GET',
            credentials: 'same-origin',
            headers: {
              'Accept': 'application/json',
              'X-Requested-With': 'XMLHttpRequest'
            }
          });

          if (!cartResponse.ok) {
            throw new Error('Gift packaging was added, but the cart could not be refreshed.');
          }

          const updatedCart = await cartResponse.json();
          const addedVariantIds = new Set(items.map((item) => String(item.id)));

          const giftItemsPresent = updatedCart.items.some((cartItem) =>
            addedVariantIds.has(String(cartItem.variant_id || cartItem.id))
          );

          if (!giftItemsPresent) {
            throw new Error('Shopify did not add the selected gift bag product(s).');
          }

          window.location.reload();
        } catch (error) {
          console.error('Gift bag add error:', error);

          addButton.disabled = false;
          addButton.textContent = normalAddText;

          /*
            Show a visible error in the drawer instead of failing silently.
          */
          let errorBox = modal.querySelector('.asl-giftwrap-modal__error');

          if (!errorBox) {
            errorBox = document.createElement('div');
            errorBox.className = 'asl-giftwrap-modal__error';
            errorBox.setAttribute('role', 'alert');

            const footer = modal.querySelector('.asl-giftwrap-modal__footer');
            footer?.insertAdjacentElement('beforebegin', errorBox);
          }

          if (errorBox) {
            errorBox.textContent = error?.message || 'Δεν ήταν δυνατή η προσθήκη της συσκευασίας δώρου.';
          }
        }
      });

      const refreshGiftWrapOffset = () => {
        if (modal.classList.contains('is-open')) {
          setGiftWrapHeaderOffset();
        }
      };

      window.addEventListener('resize', refreshGiftWrapOffset);
      window.addEventListener('orientationchange', refreshGiftWrapOffset);

      /* Sticky headers can change position/height after scrolling. */
      window.addEventListener('scroll', refreshGiftWrapOffset, { passive: true });

      setGiftWrapHeaderOffset();
      calculateTotal();
    })();
  </script>
{%- endif -%}




<script>
(() => {
  if (window.__aslCartTwoColumnLayout) return;
  window.__aslCartTwoColumnLayout = true;

  const buildCartLayout = () => {
    const items = document.getElementById('main-cart-items');
    const footer = document.getElementById('main-cart-footer');

    if (!items || !footer) return;

    const itemsSection = items.closest('.shopify-section');
    const footerSection = footer.closest('.shopify-section');

    if (!itemsSection || !footerSection) return;

    let layout = document.querySelector('.asl-cart-page-layout');

    if (!layout) {
      layout = document.createElement('div');
      layout.className = 'asl-cart-page-layout';

      itemsSection.parentNode.insertBefore(layout, itemsSection);
    }

    if (itemsSection.parentElement !== layout) {
      layout.appendChild(itemsSection);
    }

    if (footerSection.parentElement !== layout) {
      layout.appendChild(footerSection);
    }
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', buildCartLayout);
  } else {
    buildCartLayout();
  }

  document.addEventListener('shopify:section:load', buildCartLayout);
})();
</script>


<style>
@media screen and (min-width: 990px) {
  .asl-cart-page-layout {
    grid-template-columns: minmax(0, 1.9fr) minmax(380px, .9fr) !important;
    column-gap: 72px !important;
    max-width: 1540px !important;
    padding: 48px 44px 80px !important;
  }

  .asl-cart-page-layout #main-cart-footer {
    align-self: start !important;
  }

  .asl-cart-page-layout #main-cart-footer .cart__footer {
    position: sticky !important;
    top: 24px !important;
  }

  .asl-cart-page-layout #main-cart-footer .cart__note {
    margin: 0 0 20px !important;
  }

  .asl-cart-page-layout #main-cart-footer .cart__note label {
    display: block !important;
    margin-bottom: 10px !important;
    font-size: 13px !important;
    line-height: 1.2 !important;
    font-weight: 500 !important;
    color: #08044C !important;
  }

  .asl-cart-page-layout #main-cart-footer .cart__note textarea {
    min-height: 112px !important;
    border: 1px solid rgba(8, 4, 76, .28) !important;
    border-radius: 0 !important;
    background: #fff !important;
    box-shadow: none !important;
    padding: 14px 16px !important;
    font-size: 13px !important;
    color: #08044C !important;
  }

  .asl-cart-page-layout #main-cart-footer .asl-cart-giftwrap-trigger-wrap {
    margin: 0 0 6px !important;
    padding: 0 0 18px !important;
    border-bottom: 1px solid rgba(8, 4, 76, .12) !important;
  }

  .asl-cart-page-layout #main-cart-footer .asl-cart-giftwrap-trigger {
    width: 100% !important;
    justify-content: flex-start !important;
    text-decoration: none !important;
    font-size: 14px !important;
  }

  .asl-cart-page-layout #main-cart-footer .cart__blocks {
    gap: 18px !important;
  }

  .asl-cart-page-layout #main-cart-footer .totals {
    padding-top: 4px !important;
    border-top: 1px solid rgba(8, 4, 76, .12) !important;
    padding-top: 22px !important;
  }

  .asl-cart-page-layout #main-cart-footer .totals__total,
  .asl-cart-page-layout #main-cart-footer .totals__total-value {
    font-size: 17px !important;
    font-weight: 650 !important;
  }

  .asl-cart-page-layout #main-cart-footer .tax-note {
    margin: 8px 0 14px !important;
    color: rgba(8, 4, 76, .62) !important;
    font-size: 12px !important;
    line-height: 1.45 !important;
  }

  .asl-cart-page-layout #main-cart-footer #checkout {
    min-height: 52px !important;
    border-radius: 999px !important;
    letter-spacing: 0 !important;
    text-transform: none !important;
  }

  .asl-cart-page-layout #main-cart-footer .asl-checkout-payment-methods {
    margin-top: 2px !important;
    padding-top: 2px !important;
  }

  .asl-cart-page-layout #main-cart-footer .asl-checkout-payment-methods__label {
    display: none !important;
  }

  .asl-cart-page-layout #main-cart-footer .asl-checkout-payment-methods__icons {
    justify-content: flex-start !important;
    gap: 6px !important;
  }

  .asl-cart-page-layout #main-cart-footer .asl-checkout-payment-method svg {
    max-width: 40px !important;
    height: 20px !important;
  }
}
</style>


<style>
/* =========================================================
   CART SUMMARY — CLEANER RIGHT COLUMN + COLLAPSIBLE NOTE
========================================================= */

.asl-cart-accordion {
  width: 100%;
  margin: 0 0 14px;
  border: 0;
}

.asl-cart-accordion__summary {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;

  width: 100%;
  min-height: 54px;

  margin: 0;
  padding: 0 18px;

  list-style: none;
  cursor: pointer;

  border: 0;
  border-radius: 999px;

  background: #f1f1f1;
  color: #08044C;

  font-size: 14px;
  line-height: 1.2;
  font-weight: 600;

  box-sizing: border-box;
}

.asl-cart-accordion__summary::-webkit-details-marker {
  display: none;
}

.asl-cart-accordion__summary::marker {
  content: "";
}

.asl-cart-accordion__icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;

  width: 18px;
  height: 18px;
  flex: 0 0 18px;

  transition: transform .2s ease;
}

.asl-cart-accordion__icon svg {
  display: block;
  width: 14px;
  height: 14px;

  fill: none;
  stroke: currentColor;
  stroke-width: 1.5;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.asl-cart-accordion[open] .asl-cart-accordion__icon {
  transform: rotate(180deg);
}

.asl-cart-accordion__content {
  padding: 12px 0 2px;
}

.asl-cart-note-accordion .cart__note {
  display: block !important;
  width: 100% !important;
  margin: 0 !important;
}

.asl-cart-note-accordion .cart__note::before,
.asl-cart-note-accordion .cart__note::after {
  display: none !important;
}

.asl-cart-note-accordion .cart__note textarea {
  display: block !important;

  width: 100% !important;
  min-height: 92px !important;
  max-height: 150px !important;

  margin: 0 !important;
  padding: 13px 14px !important;

  border: 1px solid rgba(8, 4, 76, .20) !important;
  border-radius: 0 !important;

  background: #fff !important;
  color: #08044C !important;

  font-size: 13px !important;
  line-height: 1.4 !important;

  box-shadow: none !important;
  resize: vertical !important;

  box-sizing: border-box !important;
}

@media screen and (min-width: 990px) {

  .asl-cart-page-layout {
    grid-template-columns:
      minmax(0, 1.95fr)
      minmax(400px, .85fr) !important;

    column-gap: 72px !important;
    max-width: 1500px !important;

    padding:
      48px
      46px
      76px !important;
  }

  /* Right side becomes one compact checkout stack */
  .asl-cart-page-layout #main-cart-footer .cart__footer {
    position: sticky !important;
    top: 24px !important;

    width: 100% !important;
    max-width: none !important;

    margin: 0 !important;
    padding: 0 !important;
  }

  .asl-cart-page-layout #main-cart-footer .cart__blocks {
    display: flex !important;
    flex-direction: column !important;

    width: 100% !important;
    max-width: none !important;

    gap: 0 !important;
  }

  /* Apps always sit at the very top of the right column */
  .asl-cart-page-layout #main-cart-footer .cart__blocks > .shopify-app-block,
  .asl-cart-page-layout #main-cart-footer .cart__blocks > [data-shopify-editor-block] {
    order: -30 !important;

    width: 100% !important;
    max-width: none !important;

    margin: 0 0 14px !important;
  }

  /* Gift wrap becomes a clean row instead of a floating link */
  .asl-cart-page-layout #main-cart-footer .asl-cart-giftwrap-trigger-wrap {
    margin: 0 0 16px !important;
    padding: 0 !important;

    border: 0 !important;
  }

  .asl-cart-page-layout #main-cart-footer .asl-cart-giftwrap-trigger {
    display: flex !important;
    align-items: center !important;

    width: 100% !important;
    min-height: 54px !important;

    margin: 0 !important;
    padding: 0 18px !important;

    border: 0 !important;
    border-radius: 999px !important;

    background: #f1f1f1 !important;
    color: #08044C !important;

    text-decoration: none !important;

    font-size: 14px !important;
    font-weight: 600 !important;

    box-sizing: border-box !important;
  }

  .asl-cart-page-layout #main-cart-footer .asl-cart-giftwrap-trigger__icon {
    width: 18px !important;
    height: 18px !important;
  }

  .asl-cart-page-layout #main-cart-footer .asl-cart-giftwrap-trigger__icon svg {
    width: 18px !important;
    height: 18px !important;
  }

  /* Total block */
  .asl-cart-page-layout #main-cart-footer .js-contents {
    width: 100% !important;

    margin-top: 8px !important;
    padding-top: 18px !important;

    border-top: 1px solid rgba(8, 4, 76, .10) !important;
  }

  .asl-cart-page-layout #main-cart-footer .totals {
    display: flex !important;
    align-items: baseline !important;
    justify-content: space-between !important;
    gap: 20px !important;

    width: 100% !important;

    margin: 0 !important;
    padding: 0 !important;

    border: 0 !important;
  }

  .asl-cart-page-layout #main-cart-footer .totals__total,
  .asl-cart-page-layout #main-cart-footer .totals__total-value {
    margin: 0 !important;

    color: #08044C !important;

    font-size: 17px !important;
    line-height: 1.2 !important;

    font-weight: 650 !important;
  }

  .asl-cart-page-layout #main-cart-footer .tax-note {
    display: block !important;

    margin: 7px 0 20px !important;

    color: rgba(8, 4, 76, .55) !important;

    font-size: 11px !important;
    line-height: 1.45 !important;

    text-align: left !important;
  }

  /* Checkout */
  .asl-cart-page-layout #main-cart-footer .cart__ctas {
    width: 100% !important;
    margin: 0 !important;
  }

  .asl-cart-page-layout #main-cart-footer #checkout {
    width: 100% !important;
    min-height: 52px !important;

    margin: 0 !important;
    padding: 0 20px !important;

    border: 0 !important;
    border-radius: 999px !important;

    background: #08044C !important;
    color: #fff !important;

    font-size: 14px !important;
    font-weight: 600 !important;

    box-shadow: none !important;
  }

  /* Payment methods */
  .asl-cart-page-layout #main-cart-footer .asl-checkout-payment-methods {
    margin-top: 14px !important;
  }

  .asl-cart-page-layout #main-cart-footer .asl-checkout-payment-methods__label {
    display: none !important;
  }

  .asl-cart-page-layout #main-cart-footer .asl-checkout-payment-methods__icons {
    justify-content: center !important;
    gap: 6px !important;
  }

  .asl-cart-page-layout #main-cart-footer .asl-checkout-payment-method svg {
    max-width: 36px !important;
    height: 19px !important;
  }
}

@media screen and (max-width: 989px) {
  .asl-cart-accordion__summary {
    min-height: 50px;
    padding-inline: 16px;
    font-size: 13px;
  }
}
</style>


<script>
(() => {
  const fixSummary = () => {
    const footer = document.getElementById('main-cart-footer');
    if (!footer) return;

    const note = footer.querySelector('.asl-cart-note-accordion');
    const gift = footer.querySelector('.asl-cart-giftwrap-trigger-wrap');

    /* ONLY move Shopify app block(s) above Notes.
       Do not move totals, prices, checkout, or any other cart content. */
    if (note) {
      const appBlocks = Array.from(
        footer.querySelectorAll(
          '.cart__blocks > .shopify-app-block, .cart__blocks > [data-shopify-editor-block]'
        )
      );

      appBlocks.forEach((appBlock) => {
        note.insertAdjacentElement('beforebegin', appBlock);
      });
    }

    if (note && gift && note.nextElementSibling !== gift) {
      note.insertAdjacentElement('afterend', gift);
    }

    const checkout = footer.querySelector('.cart__ctas:not(.cart__ctas--klarna)');
    const accelerated = footer.querySelector('.cart__dynamic-checkout-buttons');
    const klarna = footer.querySelector('.cart__ctas--klarna');
    const payments = footer.querySelector('.asl-checkout-payment-methods');

    /*
      Keep checkout methods in this exact order:
      1. Main checkout
      2. Shopify accelerated/additional checkout buttons (when available)
      3. Klarna — always last checkout CTA
      4. Payment method icons
    */
    if (checkout) {
      let anchor = checkout;

      if (accelerated) {
        anchor.insertAdjacentElement('afterend', accelerated);
        anchor = accelerated;
      }

      if (klarna) {
        anchor.insertAdjacentElement('afterend', klarna);
        anchor = klarna;
      }

      if (payments) {
        anchor.insertAdjacentElement('afterend', payments);
      }
    }
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', fixSummary);
  } else {
    fixSummary();
  }

  document.addEventListener('shopify:section:load', fixSummary);
})();
</script>


<style>
/* =========================================================
   FINAL CART SUMMARY FIX — MUST LIVE IN THIS SECTION FILE
   (Loads after base.css, so it actually wins.)
========================================================= */
@media screen and (min-width: 990px) {

  /* same exact outer width for note and gift wrap */
  #main-cart-footer .asl-cart-note-accordion,
  #main-cart-footer .asl-cart-giftwrap-trigger-wrap {
    display: block !important;
    width: 100% !important;
    max-width: none !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
    box-sizing: border-box !important;
  }

  #main-cart-footer .asl-cart-note-accordion {
    margin-bottom: 10px !important;
  }

  #main-cart-footer .asl-cart-giftwrap-trigger-wrap {
    margin-bottom: 28px !important;
  }

  /* exact same pill dimensions */
  #main-cart-footer .asl-cart-accordion__summary,
  #main-cart-footer .asl-cart-giftwrap-trigger {
    display: flex !important;
    align-items: center !important;

    width: 100% !important;
    max-width: none !important;

    height: 54px !important;
    min-height: 54px !important;

    margin: 0 !important;
    padding: 0 18px !important;

    border: 0 !important;
    border-radius: 999px !important;

    background: #f1f1f1 !important;
    color: #08044C !important;

    box-sizing: border-box !important;
  }

  #main-cart-footer .asl-cart-accordion__summary {
    justify-content: space-between !important;
  }

  #main-cart-footer .asl-cart-giftwrap-trigger {
    justify-content: flex-start !important;
    gap: 10px !important;
  }

  /* align text baselines */
  #main-cart-footer .asl-cart-accordion__summary > span:first-child,
  #main-cart-footer .asl-cart-giftwrap-trigger > span:last-child {
    display: inline-flex !important;
    align-items: center !important;

    margin: 0 !important;
    padding: 0 !important;

    font-size: 13px !important;
    line-height: 1 !important;
    font-weight: 600 !important;
  }

  #main-cart-footer .asl-cart-giftwrap-trigger__icon,
  #main-cart-footer .asl-cart-giftwrap-trigger__icon svg {
    width: 19px !important;
    height: 19px !important;
    min-width: 19px !important;
    flex: 0 0 19px !important;
  }

  /* checkout: exact width, no Dawn outline/border */
  #main-cart-footer .cart__ctas {
    width: 100% !important;
    max-width: none !important;
    margin: 0 !important;
    padding: 0 !important;
    border: 0 !important;
    outline: 0 !important;
    box-shadow: none !important;
  }

  #main-cart-footer #checkout {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;

    width: 100% !important;
    max-width: none !important;

    height: 52px !important;
    min-height: 52px !important;

    margin: 0 !important;
    padding: 0 22px !important;

    border: 0 !important;
    outline: 0 !important;
    border-radius: 999px !important;

    background: #08044C !important;
    color: #fff !important;

    box-shadow: none !important;
    box-sizing: border-box !important;
  }

  #main-cart-footer #checkout::before,
  #main-cart-footer #checkout::after,
  #main-cart-footer .cart__ctas::before,
  #main-cart-footer .cart__ctas::after {
    display: none !important;
    content: none !important;
    box-shadow: none !important;
  }

  /* bigger payment icons on desktop */
  #main-cart-footer .asl-checkout-payment-methods {
    width: 100% !important;
    max-width: none !important;
    margin: 16px 0 0 !important;
    padding: 0 !important;
  }

  #main-cart-footer .asl-checkout-payment-methods__icons {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    flex-wrap: wrap !important;

    width: 100% !important;
    gap: 8px !important;
  }

  #main-cart-footer .asl-checkout-payment-method {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;

    width: auto !important;
    height: 30px !important;

    margin: 0 !important;
    padding: 0 !important;

    border: 0 !important;
    background: transparent !important;
  }

  #main-cart-footer .asl-checkout-payment-method svg {
    display: block !important;

    width: auto !important;
    max-width: none !important;
    height: 28px !important;

    transform: none !important;
  }
}
</style>


<style>
/* =========================================================
   CART SUMMARY — EXACT DESKTOP ALIGNMENT
   Fixes Dawn's .cart__footer > * + * { margin-left: 4rem; }
========================================================= */
@media screen and (min-width: 990px) {

  /* THIS is what was shifting subtotal / checkout to the right */
  #main-cart-footer .cart__footer > * + * {
    margin-left: 0 !important;
  }

  #main-cart-footer .cart__footer,
  #main-cart-footer .cart__blocks,
  #main-cart-footer .asl-cart-note-accordion,
  #main-cart-footer .asl-cart-giftwrap-trigger-wrap,
  #main-cart-footer .js-contents,
  #main-cart-footer .cart__ctas,
  #main-cart-footer .asl-checkout-payment-methods {
    width: 100% !important;
    max-width: none !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
    box-sizing: border-box !important;
  }

  /* Notes + gift wrap: identical edges */
  #main-cart-footer .asl-cart-accordion__summary,
  #main-cart-footer .asl-cart-giftwrap-trigger {
    width: 100% !important;
    max-width: none !important;
    height: 54px !important;
    min-height: 54px !important;

    margin: 0 !important;
    padding: 0 18px !important;

    border: 0 !important;
    border-radius: 999px !important;

    box-sizing: border-box !important;
  }

  #main-cart-footer .asl-cart-note-accordion {
    margin-bottom: 10px !important;
  }

  #main-cart-footer .asl-cart-giftwrap-trigger-wrap {
    margin-bottom: 28px !important;
  }

  /* Total / checkout line up with the pills */
  #main-cart-footer .totals,
  #main-cart-footer #checkout {
    width: 100% !important;
    max-width: none !important;
    box-sizing: border-box !important;
  }

  /* Checkout — no Dawn pseudo-border */
  #main-cart-footer .cart__ctas {
    padding: 0 !important;
    border: 0 !important;
    box-shadow: none !important;
  }

  #main-cart-footer #checkout {
    height: 52px !important;
    min-height: 52px !important;

    margin: 0 !important;
    padding: 0 22px !important;

    border: 0 !important;
    outline: 0 !important;
    border-radius: 999px !important;

    background: #08044C !important;
    color: #fff !important;

    box-shadow: none !important;
  }

  #main-cart-footer #checkout::before,
  #main-cart-footer #checkout::after,
  #main-cart-footer .cart__ctas::before,
  #main-cart-footer .cart__ctas::after {
    content: none !important;
    display: none !important;
    box-shadow: none !important;
  }

  /* PAYMENT ICONS — visibly larger on desktop */
  #main-cart-footer .asl-checkout-payment-methods {
    margin-top: 16px !important;
    padding: 0 !important;
  }

  #main-cart-footer .asl-checkout-payment-methods__icons {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    flex-wrap: wrap !important;

    width: 100% !important;
    gap: 8px !important;
  }

  #main-cart-footer .asl-checkout-payment-method {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;

    width: 46px !important;
    height: 30px !important;

    margin: 0 !important;
    padding: 0 !important;

    border: 0 !important;
    background: transparent !important;
  }

  #main-cart-footer .asl-checkout-payment-method svg {
    display: block !important;

    width: 46px !important;
    height: 30px !important;
    max-width: 46px !important;
    max-height: 30px !important;

    object-fit: contain !important;
  }
}
</style>


<style>
/* =========================================================
   PAYMENT ICONS — MEDIUM DESKTOP SIZE
   This lives in the section, so it wins over base.css.
========================================================= */
@media screen and (min-width: 990px) {

  #main-cart-footer .asl-checkout-payment-methods {
    width: 100% !important;
    margin-top: 16px !important;
    padding: 0 !important;
  }

  #main-cart-footer .asl-checkout-payment-methods__icons {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    flex-wrap: wrap !important;

    width: 100% !important;
    gap: 8px !important;
  }

  #main-cart-footer .asl-checkout-payment-method {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;

    width: 46px !important;
    min-width: 46px !important;
    height: 30px !important;
    min-height: 30px !important;

    margin: 0 !important;
    padding: 0 !important;

    border: 0 !important;
    background: transparent !important;
    overflow: visible !important;
  }

  #main-cart-footer .asl-checkout-payment-method svg {
    display: block !important;

    width: 42px !important;
    min-width: 42px !important;
    max-width: 42px !important;

    height: 26px !important;
    min-height: 26px !important;
    max-height: 26px !important;

    margin: 0 !important;

    transform: none !important;
    overflow: visible !important;
  }
}
</style>


<style>
/* =========================================================
   ASLANIS CART — CHECKOUT BUTTON SIZE + KLARNA FINAL CTA
   Klarna brand colors sampled from the supplied badge:
   Pink #FFA8CD / Ink #0B051D
========================================================= */

#main-cart-footer {
  --asl-checkout-height: 52px;
  --asl-klarna-pink: #FFA8CD;
  --asl-klarna-ink: #0B051D;
}

/* Main checkout and Klarna: exact same outer geometry */
#main-cart-footer .cart__ctas,
#main-cart-footer .cart__ctas--klarna {
  width: 100% !important;
  max-width: none !important;
  margin-left: 0 !important;
  margin-right: 0 !important;
  padding: 0 !important;
  box-sizing: border-box !important;
}

#main-cart-footer #checkout,
#main-cart-footer #checkout-klarna {
  width: 100% !important;
  max-width: none !important;
  height: var(--asl-checkout-height) !important;
  min-height: var(--asl-checkout-height) !important;
  max-height: var(--asl-checkout-height) !important;
  margin: 0 !important;
  padding: 0 22px !important;
  border: 0 !important;
  border-radius: 999px !important;
  box-shadow: none !important;
  box-sizing: border-box !important;
}

/* Klarna */
#main-cart-footer .cart__ctas--klarna {
  margin-top: 10px !important;
}

#main-cart-footer #checkout-klarna {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  background: var(--asl-klarna-pink) !important;
  color: var(--asl-klarna-ink) !important;
}

#main-cart-footer #checkout-klarna::before,
#main-cart-footer #checkout-klarna::after {
  display: none !important;
  content: none !important;
  box-shadow: none !important;
}

#main-cart-footer .asl-klarna-checkout__logo {
  display: block !important;
  width: auto !important;
  height: 34px !important;
  max-width: 132px !important;
  object-fit: contain !important;
}

/* Because the supplied logo already uses Klarna pink,
   matching the button background makes the badge blend into the button. */
#main-cart-footer #checkout-klarna:hover {
  background: var(--asl-klarna-pink) !important;
  color: var(--asl-klarna-ink) !important;
  opacity: .90 !important;
  transform: translateY(-1px) !important;
}

#main-cart-footer #checkout-klarna:disabled {
  opacity: .45 !important;
  cursor: not-allowed !important;
  transform: none !important;
}

/* =========================================================
   SHOPIFY ADDITIONAL / ACCELERATED CHECKOUT
   Match the 52px height and full width of main checkout.
   Includes Shopify's newer accelerated-checkout web component vars.
========================================================= */

#main-cart-footer .cart__dynamic-checkout-buttons,
#main-cart-footer .additional-checkout-buttons {
  width: 100% !important;
  max-width: none !important;
  margin: 10px 0 0 !important;
  padding: 0 !important;
  box-sizing: border-box !important;

  --shopify-accelerated-checkout-button-height: var(--asl-checkout-height);
  --shopify-accelerated-checkout-button-border-radius: 999px;
  --shopify-accelerated-checkout-row-gap: 10px;
  --shopify-accelerated-checkout-inline-alignment: stretch;
}

#main-cart-footer shopify-accelerated-checkout-cart,
#main-cart-footer shopify-accelerated-checkout {
  display: block !important;
  width: 100% !important;
  max-width: none !important;
}

/* Legacy / fallback accelerated checkout markup */
#main-cart-footer .cart__dynamic-checkout-buttons ul,
#main-cart-footer .additional-checkout-buttons ul {
  width: 100% !important;
  max-width: none !important;
  margin: 0 !important;
  padding: 0 !important;
}

#main-cart-footer .cart__dynamic-checkout-buttons li,
#main-cart-footer .additional-checkout-buttons li {
  width: 100% !important;
  max-width: none !important;
  min-height: var(--asl-checkout-height) !important;
  margin: 0 0 10px !important;
  padding: 0 !important;
}

#main-cart-footer .cart__dynamic-checkout-buttons li:last-child,
#main-cart-footer .additional-checkout-buttons li:last-child {
  margin-bottom: 0 !important;
}

#main-cart-footer .cart__dynamic-checkout-buttons button,
#main-cart-footer .cart__dynamic-checkout-buttons [role="button"],
#main-cart-footer .cart__dynamic-checkout-buttons iframe,
#main-cart-footer .additional-checkout-buttons button,
#main-cart-footer .additional-checkout-buttons [role="button"],
#main-cart-footer .additional-checkout-buttons iframe {
  width: 100% !important;
  max-width: none !important;
  height: var(--asl-checkout-height) !important;
  min-height: var(--asl-checkout-height) !important;
  border-radius: 999px !important;
  box-sizing: border-box !important;
}

/* Explicit visual order as a safety net */
#main-cart-footer .cart__ctas:not(.cart__ctas--klarna) {
  order: 4 !important;
}

#main-cart-footer .cart__dynamic-checkout-buttons {
  order: 5 !important;
}

#main-cart-footer .cart__ctas--klarna {
  order: 6 !important;
}

#main-cart-footer .asl-checkout-payment-methods {
  order: 7 !important;
}

@media screen and (max-width: 749px) {
  #main-cart-footer {
    --asl-checkout-height: 50px;
  }

  #main-cart-footer .asl-klarna-checkout__logo {
    height: 31px !important;
    max-width: 120px !important;
  }

  #main-cart-footer .cart__dynamic-checkout-buttons,
  #main-cart-footer .additional-checkout-buttons,
  #main-cart-footer .cart__ctas--klarna {
    margin-top: 8px !important;
  }
}
</style>


<style>
/* =========================================================
   ASLANIS CART — FINAL CHECKOUT BUTTON CLEANUP
   - removes Dawn's visible outer box on mobile
   - makes checkout / accelerated / Klarna spacing consistent
========================================================= */

/* Remove Dawn button/wrapper outlines everywhere */
#main-cart-footer .cart__ctas,
#main-cart-footer .cart__ctas::before,
#main-cart-footer .cart__ctas::after,
#main-cart-footer .cart__checkout-button,
#main-cart-footer .cart__checkout-button::before,
#main-cart-footer .cart__checkout-button::after {
  border: 0 !important;
  outline: 0 !important;
  box-shadow: none !important;
}

#main-cart-footer .cart__ctas::before,
#main-cart-footer .cart__ctas::after,
#main-cart-footer .cart__checkout-button::before,
#main-cart-footer .cart__checkout-button::after {
  content: none !important;
  display: none !important;
}

/* Desktop: clean, even vertical rhythm */
@media screen and (min-width: 990px) {
  #main-cart-footer .cart__ctas:not(.cart__ctas--klarna) {
    margin: 0 !important;
  }

  #main-cart-footer .cart__dynamic-checkout-buttons,
  #main-cart-footer .additional-checkout-buttons {
    margin: 12px 0 0 !important;
  }

  #main-cart-footer .cart__ctas--klarna {
    margin: 12px 0 0 !important;
  }

  #main-cart-footer .asl-checkout-payment-methods {
    margin-top: 14px !important;
  }
}

/* Mobile: remove the rectangular box around the pill button */
@media screen and (max-width: 989px) {
  #main-cart-footer .cart__ctas,
  #main-cart-footer .cart__ctas--klarna {
    width: 100% !important;
    max-width: none !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
    padding: 0 !important;

    border: 0 !important;
    outline: 0 !important;
    box-shadow: none !important;
    background: transparent !important;
  }

  #main-cart-footer #checkout,
  #main-cart-footer #checkout-klarna {
    width: 100% !important;
    max-width: none !important;
    margin: 0 !important;

    border: 0 !important;
    outline: 0 !important;
    box-shadow: none !important;
  }

  #main-cart-footer .cart__dynamic-checkout-buttons,
  #main-cart-footer .additional-checkout-buttons,
  #main-cart-footer .cart__ctas--klarna {
    margin-top: 8px !important;
  }

  #main-cart-footer .asl-checkout-payment-methods {
    margin-top: 12px !important;
  }
}
</style>


<style>
/* =========================================================
   ASLANIS CART — CHECKOUT STACK, FINAL DESKTOP + MOBILE FIX
========================================================= */

#main-cart-footer .asl-checkout-stack {
  width: 100% !important;
  max-width: none !important;

  display: grid !important;
  grid-template-columns: 1fr !important;

  margin: 0 !important;
  padding: 0 !important;

  box-sizing: border-box !important;
}

/* The stack itself controls all spacing. */
#main-cart-footer .asl-checkout-stack > .cart__ctas,
#main-cart-footer .asl-checkout-stack > .cart__dynamic-checkout-buttons,
#main-cart-footer .asl-checkout-stack > .additional-checkout-buttons,
#main-cart-footer .asl-checkout-stack > .asl-checkout-payment-methods {
  width: 100% !important;
  max-width: none !important;

  margin: 0 !important;
  padding-left: 0 !important;
  padding-right: 0 !important;

  box-sizing: border-box !important;
}

/* Remove Dawn's rectangular wrapper / pseudo outline on BOTH desktop + mobile */
#main-cart-footer .asl-checkout-stack .cart__ctas,
#main-cart-footer .asl-checkout-stack .cart__ctas::before,
#main-cart-footer .asl-checkout-stack .cart__ctas::after,
#main-cart-footer .asl-checkout-stack .button,
#main-cart-footer .asl-checkout-stack .button::before,
#main-cart-footer .asl-checkout-stack .button::after {
  border: 0 !important;
  outline: 0 !important;
  box-shadow: none !important;
}

#main-cart-footer .asl-checkout-stack .cart__ctas::before,
#main-cart-footer .asl-checkout-stack .cart__ctas::after,
#main-cart-footer .asl-checkout-stack .button::before,
#main-cart-footer .asl-checkout-stack .button::after {
  content: none !important;
  display: none !important;
}

/* Main + Klarna identical geometry */
#main-cart-footer .asl-checkout-stack #checkout,
#main-cart-footer .asl-checkout-stack #checkout-klarna {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;

  width: 100% !important;
  max-width: none !important;

  height: 52px !important;
  min-height: 52px !important;
  max-height: 52px !important;

  margin: 0 !important;
  padding: 0 22px !important;

  border: 0 !important;
  outline: 0 !important;
  border-radius: 999px !important;

  box-shadow: none !important;
  box-sizing: border-box !important;
}

/* Shopify accelerated checkout also gets the exact same requested height */
#main-cart-footer .asl-checkout-stack .cart__dynamic-checkout-buttons,
#main-cart-footer .asl-checkout-stack .additional-checkout-buttons {
  --shopify-accelerated-checkout-button-height: 52px !important;
  --shopify-accelerated-checkout-button-border-radius: 999px !important;
  --shopify-accelerated-checkout-row-gap: 12px !important;
  --shopify-accelerated-checkout-inline-alignment: stretch !important;
}

#main-cart-footer .asl-checkout-stack shopify-accelerated-checkout-cart,
#main-cart-footer .asl-checkout-stack shopify-accelerated-checkout {
  display: block !important;
  width: 100% !important;
  max-width: none !important;
}

/* DESKTOP — force visible, even spacing between every checkout CTA */
@media screen and (min-width: 990px) {
  #main-cart-footer .asl-checkout-stack {
    row-gap: 12px !important;
  }

  #main-cart-footer .asl-checkout-stack > * {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
  }

  /* Payment icons need a little extra separation after Klarna */
  #main-cart-footer .asl-checkout-stack > .asl-checkout-payment-methods {
    margin-top: 4px !important;
  }
}

/* MOBILE */
@media screen and (max-width: 989px) {
  #main-cart-footer .asl-checkout-stack {
    row-gap: 8px !important;
  }

  #main-cart-footer .asl-checkout-stack > * {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
  }

  #main-cart-footer .asl-checkout-stack #checkout,
  #main-cart-footer .asl-checkout-stack #checkout-klarna {
    height: 50px !important;
    min-height: 50px !important;
    max-height: 50px !important;
  }

  #main-cart-footer .asl-checkout-stack .cart__dynamic-checkout-buttons,
  #main-cart-footer .asl-checkout-stack .additional-checkout-buttons {
    --shopify-accelerated-checkout-button-height: 50px !important;
    --shopify-accelerated-checkout-row-gap: 8px !important;
  }

  #main-cart-footer .asl-checkout-stack > .asl-checkout-payment-methods {
    margin-top: 4px !important;
  }
}
</style>

{% schema %}
{
  "name": "t:sections.main-cart-footer.name",
  "class": "cart__footer-wrapper",
  "settings": [
    {
      "type": "header",
      "content": "Delivery popup — content"
    },
    {
      "type": "text",
      "id": "delivery_title",
      "label": "Popup title",
      "default": "Πώς θέλετε να παραλάβετε;"
    },
    {
      "type": "richtext",
      "id": "delivery_description",
      "label": "Popup description",
      "default": "<p>Επιλέξτε τρόπο παράδοσης πριν συνεχίσετε στο checkout.</p>"
    },
    {
      "type": "text",
      "id": "delivery_courier_title",
      "label": "Courier title",
      "default": "Παράδοση με courier"
    },
    {
      "type": "text",
      "id": "delivery_courier_subtitle",
      "label": "Courier description",
      "default": "Στη διεύθυνσή σας"
    },
    {
      "type": "image_picker",
      "id": "delivery_courier_logo",
      "label": "Courier primary logo"
    },
    {
      "type": "image_picker",
      "id": "delivery_courier_logo_2",
      "label": "Courier second logo (plus hover)"
    },
    {
      "type": "text",
      "id": "delivery_boxnow_title",
      "label": "BOX NOW title",
      "default": "BOX NOW Locker"
    },
    {
      "type": "text",
      "id": "delivery_boxnow_subtitle",
      "label": "BOX NOW description",
      "default": "Παραλαβή από αυτόματο locker"
    },
    {
      "type": "image_picker",
      "id": "delivery_boxnow_logo",
      "label": "BOX NOW primary logo"
    },
    {
      "type": "image_picker",
      "id": "delivery_boxnow_logo_2",
      "label": "BOX NOW second logo (plus hover)"
    },
    {"type":"header","content":"ACS Smartpoint lockers"},
    {"type":"text","id":"delivery_acs_title","label":"ACS option title","default":"ACS Smartpoint Locker"},
    {"type":"text","id":"delivery_acs_subtitle","label":"ACS option subtitle","default":"Παραλαβή από ACS locker"},
    {"type":"image_picker","id":"delivery_acs_logo","label":"ACS primary logo"},
    {"type":"image_picker","id":"delivery_acs_logo_2","label":"ACS second logo (plus hover)"},
    {"type":"text","id":"delivery_acs_heading","label":"ACS selector heading","default":"Επιλέξτε ACS locker"},
    {"type":"text","id":"delivery_acs_help","label":"ACS selector help","default":"Αναζητήστε και επιλέξτε το σημείο παραλαβής σας."},
    {"type":"text","id":"delivery_acs_search_placeholder","label":"ACS search placeholder","default":"Πόλη, ΤΚ ή locker..."},
    {"type":"text","id":"delivery_acs_json_url","label":"ACS JSON feed URL","info":"Use a current HTTPS ACS station feed with GR country codes and locker types 8/12. All matching Greek lockers and addresses are shown. Never place API secrets here."},
    {
      "type": "text",
      "id": "delivery_map_heading",
      "label": "Locker map heading",
      "default": "Επιλέξτε locker"
    },
    {
      "type": "textarea",
      "id": "delivery_map_notice",
      "label": "Text below BOX NOW map",
      "default": "Επιλέξτε locker χρησιμοποιώντας τον χάρτη BOX NOW πριν προχωρήσετε."
    },
    {
      "type": "text",
      "id": "delivery_continue_text",
      "label": "Continue button",
      "default": "Συνέχεια στο checkout"
    },
    {
      "type": "text",
      "id": "delivery_saving_text",
      "label": "Saving button",
      "default": "Αποθήκευση…"
    },
    {
      "type": "text",
      "id": "delivery_close_label",
      "label": "Close accessibility label",
      "default": "Κλείσιμο"
    },
    {
      "type": "text",
      "id": "delivery_required_error",
      "label": "Missing method message",
      "default": "Επιλέξτε Courier ή BOX NOW Locker."
    },
    {
      "type": "textarea",
      "id": "delivery_missing_map",
      "label": "Missing BOX NOW map message",
      "default": "Δεν βρέθηκε ενεργό BOX NOW app block. Προσθέστε το BOX NOW Lockers Map στο Cart από το Theme Editor και ενεργοποιήστε το App Embed."
    },
    {
      "type": "text",
      "id": "delivery_save_error",
      "label": "Save error message",
      "default": "Δεν αποθηκεύτηκε ο τρόπος αποστολής."
    },
    {
      "type": "header",
      "content": "Delivery popup — appearance"
    },
    {
      "type": "range",
      "id": "delivery_width",
      "label": "Popup width",
      "default": 540,
      "min": 380,
      "max": 900,
      "step": 20,
      "unit": "px"
    },
    {
      "type": "range",
      "id": "delivery_padding",
      "label": "Inner padding",
      "default": 28,
      "min": 12,
      "max": 60,
      "step": 2,
      "unit": "px"
    },
    {
      "type": "range",
      "id": "delivery_title_size",
      "label": "Title size",
      "default": 28,
      "min": 18,
      "max": 44,
      "step": 1,
      "unit": "px"
    },
    {
      "type": "range",
      "id": "delivery_radius",
      "label": "Corner radius",
      "default": 5,
      "min": 0,
      "max": 32,
      "step": 1,
      "unit": "px"
    },
    {
      "type": "range",
      "id": "delivery_option_gap",
      "label": "Option spacing",
      "default": 12,
      "min": 4,
      "max": 30,
      "step": 1,
      "unit": "px"
    },
    {
      "type": "range",
      "id": "delivery_overlay_opacity",
      "label": "Overlay opacity",
      "default": 50,
      "min": 0,
      "max": 90,
      "step": 5,
      "unit": "%"
    },
    {
      "type": "color",
      "id": "delivery_overlay_color",
      "label": "Overlay color",
      "default": "#000000"
    },
    {
      "type": "color",
      "id": "delivery_bg",
      "label": "Popup background",
      "default": "#ffffff"
    },
    {
      "type": "color",
      "id": "delivery_text_color",
      "label": "Main text",
      "default": "#08044C"
    },
    {
      "type": "color",
      "id": "delivery_muted_color",
      "label": "Secondary text",
      "default": "#68677d"
    },
    {
      "type": "color",
      "id": "delivery_accent_color",
      "label": "Selection color",
      "default": "#08044C"
    },
    {
      "type": "color",
      "id": "delivery_border_color",
      "label": "Option border",
      "default": "#b9b8c9"
    },
    {
      "type": "color",
      "id": "delivery_button_bg",
      "label": "Button background",
      "default": "#08044C"
    },
    {
      "type": "color",
      "id": "delivery_button_text",
      "label": "Button text",
      "default": "#ffffff"
    },
    {
      "type": "header",
      "content": "Delivery popup — BOX NOW integration"
    },
    {
      "type": "text",
      "id": "delivery_app_selector",
      "label": "Existing BOX NOW block CSS selector"
    },
    {
      "type": "color_scheme",
      "id": "color_scheme",
      "label": "t:sections.all.colors.label",
      "default": "scheme-1"
    },
    {
      "type": "header",
      "content": "Gift packaging"
    },
    {
      "type": "image_picker",
      "id": "gift_wrap_image",
      "label": "Gift packaging popup image"
    },
    {
      "type": "text",
      "id": "gift_wrap_trigger_text",
      "label": "Cart link text",
      "default": "Προσθήκη συσκευασίας δώρου"
    },
    {
      "type": "text",
      "id": "gift_wrap_title",
      "label": "Popup title",
      "default": "Συσκευασία δώρου"
    },
    {
      "type": "richtext",
      "id": "gift_wrap_description",
      "label": "Popup description",
      "default": "<p>Επίλεξε το μέγεθος και την ποσότητα της συσκευασίας δώρου.</p>"
    },
    {
      "type": "text",
      "id": "gift_wrap_add_text",
      "label": "Add button text",
      "default": "ΠΡΟΣΘΗΚΗ ΣΤΟ ΚΑΛΑΘΙ"
    },
    {
      "type": "text",
      "id": "gift_wrap_loading_text",
      "label": "Loading text",
      "default": "ΠΡΟΣΘΗΚΗ..."
    },
    {
      "type": "header",
      "content": "Payment icons"
    },
    {
      "type": "checkbox",
      "id": "show_payment_icons",
      "label": "Show payment icons below checkout",
      "default": true
    },
    {
      "type": "text",
      "id": "payment_icons_label",
      "label": "Payment icons label",
      "default": "ΤΡΟΠΟΙ ΠΛΗΡΩΜΗΣ"
    },
    {
      "type": "header",
      "content": "t:sections.all.padding.section_padding_heading"
    },
    {
      "type": "range",
      "id": "padding_top",
      "min": 0,
      "max": 100,
      "step": 4,
      "unit": "px",
      "label": "t:sections.all.padding.padding_top",
      "default": 40
    },
    {
      "type": "range",
      "id": "padding_bottom",
      "min": 0,
      "max": 100,
      "step": 4,
      "unit": "px",
      "label": "t:sections.all.padding.padding_bottom",
      "default": 40
    },
    {
      "type": "header",
      "content": "Klarna checkout button"
    },
    {
      "type": "checkbox",
      "id": "show_klarna_checkout",
      "label": "Show Klarna checkout button",
      "default": true
    },
    {
      "type": "range",
      "id": "klarna_min_cart_amount",
      "label": "Show Klarna from cart amount",
      "min": 0,
      "max": 500,
      "step": 5,
      "unit": "€",
      "default": 30
    }
  ],
  "blocks": [
    {
      "type": "subtotal",
      "name": "t:sections.main-cart-footer.blocks.subtotal.name",
      "limit": 1
    },
    {
      "type": "buttons",
      "name": "t:sections.main-cart-footer.blocks.buttons.name",
      "limit": 1
    },
    {
      "type": "gift_bag_small",
      "name": "Gift bag — Small",
      "limit": 1,
      "settings": [
        {
          "type": "product",
          "id": "product",
          "label": "Small bag product"
        },
        {
          "type": "text",
          "id": "label",
          "label": "Display label",
          "default": "Μικρό"
        }
      ]
    },
    {
      "type": "gift_bag_medium",
      "name": "Gift bag — Medium",
      "limit": 1,
      "settings": [
        {
          "type": "product",
          "id": "product",
          "label": "Medium bag product"
        },
        {
          "type": "text",
          "id": "label",
          "label": "Display label",
          "default": "Μεσαίο"
        }
      ]
    },
    {
      "type": "@app"
    }
  ]
}
{% endschema %}


<style>
/* =========================================================
   EMPTY CART — DESKTOP FULL-WIDTH CENTER FIX
   The footer section wrapper was still occupying grid column 2.
========================================================= */
@media screen and (min-width: 990px) {

  /* When the cart footer itself is marked empty, collapse the custom
     2-column cart layout to ONE full-width column. */
  .asl-cart-page-layout:has(#main-cart-footer.is-empty) {
    display: grid !important;
    grid-template-columns: minmax(0, 1fr) !important;
    column-gap: 0 !important;
    width: 100% !important;
    max-width: 1540px !important;
    margin-left: auto !important;
    margin-right: auto !important;
  }

  /* Hide the Shopify SECTION wrapper of the empty footer too.
     Hiding only #main-cart-footer leaves its parent as a grid item. */
  .asl-cart-page-layout:has(#main-cart-footer.is-empty)
    > .shopify-section:has(#main-cart-footer.is-empty) {
    display: none !important;
  }

  /* Make the cart-items section occupy the full single column. */
  .asl-cart-page-layout:has(#main-cart-footer.is-empty)
    > .shopify-section:has(#main-cart-items) {
    width: 100% !important;
    max-width: none !important;
    grid-column: 1 / -1 !important;
    margin: 0 !important;
  }

  .asl-cart-page-layout:has(#main-cart-footer.is-empty)
    #main-cart-items {
    width: 100% !important;
    max-width: none !important;
    margin: 0 auto !important;
  }

  /* Dawn empty-cart content */
  .asl-cart-page-layout:has(#main-cart-footer.is-empty)
    #main-cart-items .cart__warnings {
    width: 100% !important;
    max-width: none !important;
    margin-left: auto !important;
    margin-right: auto !important;
    text-align: center !important;
  }

  .asl-cart-page-layout:has(#main-cart-footer.is-empty)
    #main-cart-items .cart__empty-text,
  .asl-cart-page-layout:has(#main-cart-footer.is-empty)
    #main-cart-items .cart__login-title,
  .asl-cart-page-layout:has(#main-cart-footer.is-empty)
    #main-cart-items .cart__warnings p {
    text-align: center !important;
  }
}
</style>

<style>
/* =========================================================
   GIFT BAG DRAWER — HEADER OVERLAP FINAL SAFEGUARD
   ========================================================= */
#AslGiftWrapModal-{{ section.id }} {
  top: var(--asl-giftwrap-header-offset, 0px) !important;
  right: 0 !important;
  bottom: 0 !important;
  left: 0 !important;

  height: auto !important;
  max-height: calc(100dvh - var(--asl-giftwrap-header-offset, 0px)) !important;
}

#AslGiftWrapModal-{{ section.id }} .asl-giftwrap-modal__overlay {
  position: absolute !important;
  inset: 0 !important;
}

#AslGiftWrapModal-{{ section.id }} .asl-giftwrap-modal__panel {
  top: 0 !important;
  right: 0 !important;
  bottom: 0 !important;

  height: auto !important;
  max-height: 100% !important;
}

/* Keep the actual store header visually above the drawer. */
.shopify-section-group-header-group,
.section-header,
sticky-header {
  position: relative;
  z-index: 100000;
}
</style>


<style>
/* FINAL CHECKOUT BUTTON — SQUARE CORNERS */
#main-cart-footer {
  --buttons-radius: 0px !important;
  --buttons-radius-outset: 0px !important;
}
#main-cart-footer #checkout,
.asl-cart-page-layout #main-cart-footer #checkout,
#main-cart-footer .cart__checkout-button {
  border-radius: 0 !important;
}
#main-cart-footer #checkout::before,
#main-cart-footer #checkout::after,
.asl-cart-page-layout #main-cart-footer #checkout::before,
.asl-cart-page-layout #main-cart-footer #checkout::after,
#main-cart-footer .cart__checkout-button::before,
#main-cart-footer .cart__checkout-button::after {
  border-radius: 0 !important;
}
</style>

<style>
/* =========================================================
   SAFE CHECKOUT SPACING FIX
   Only removes the extra outer spacing.
   Does NOT touch Shop Pay internals, heights, custom elements,
   accelerated checkout variables, or payment button rendering.
   ========================================================= */

/* Main checkout wrapper */
#main-cart-footer .cart__ctas,
.asl-cart-page-layout #main-cart-footer .cart__ctas {
  margin-top: 0 !important;
  margin-bottom: 0 !important;
}

/* Shopify accelerated checkout / Shop Pay wrapper */
#main-cart-footer .cart__dynamic-checkout-buttons,
#main-cart-footer .additional-checkout-buttons,
.asl-cart-page-layout #main-cart-footer .cart__dynamic-checkout-buttons,
.asl-cart-page-layout #main-cart-footer .additional-checkout-buttons {
  margin-top: 8px !important;
  margin-bottom: 0 !important;
  padding-top: 0 !important;
  padding-bottom: 0 !important;
}

/* Payment icons: small, controlled space below accelerated checkout */
#main-cart-footer .asl-checkout-payment-methods,
.asl-cart-page-layout #main-cart-footer .asl-checkout-payment-methods {
  margin-top: 8px !important;
}

/* Keep checkout square — leave Shop Pay itself untouched */
#main-cart-footer #checkout,
.asl-cart-page-layout #main-cart-footer #checkout {
  border-radius: 0 !important;
}

#main-cart-footer #checkout::before,
#main-cart-footer #checkout::after,
.asl-cart-page-layout #main-cart-footer #checkout::before,
.asl-cart-page-layout #main-cart-footer #checkout::after {
  border-radius: 0 !important;
}
</style>

<style>
/* =========================================================
   FINAL GAP FIX — ONLY CONTROLS SPACE BETWEEN CHECKOUT + SHOP PAY
   ========================================================= */

/* Your file already uses a grid for .asl-checkout-stack.
   The previous rule added BOTH grid gap + margin, which doubled the space.
   From now on the grid gap is the ONLY spacing source. */
#main-cart-footer .asl-checkout-stack,
.asl-cart-page-layout #main-cart-footer .asl-checkout-stack {
  row-gap: 4px !important;
  column-gap: 0 !important;
}

/* Remove margins from the direct checkout-stack children so they cannot
   add on top of the 4px grid gap. */
#main-cart-footer .asl-checkout-stack > .cart__ctas,
#main-cart-footer .asl-checkout-stack > .cart__dynamic-checkout-buttons,
#main-cart-footer .asl-checkout-stack > .additional-checkout-buttons,
.asl-cart-page-layout #main-cart-footer .asl-checkout-stack > .cart__ctas,
.asl-cart-page-layout #main-cart-footer .asl-checkout-stack > .cart__dynamic-checkout-buttons,
.asl-cart-page-layout #main-cart-footer .asl-checkout-stack > .additional-checkout-buttons {
  margin-top: 0 !important;
  margin-bottom: 0 !important;
}

/* Payment icons can have a little more breathing room without affecting
   the checkout-to-Shop-Pay spacing. */
#main-cart-footer .asl-checkout-stack > .asl-checkout-payment-methods,
.asl-cart-page-layout #main-cart-footer .asl-checkout-stack > .asl-checkout-payment-methods {
  margin-top: 4px !important;
  margin-bottom: 0 !important;
}

/* Preserve the square main checkout button. */
#main-cart-footer #checkout,
.asl-cart-page-layout #main-cart-footer #checkout {
  border-radius: 0 !important;
}

#main-cart-footer #checkout::before,
#main-cart-footer #checkout::after,
.asl-cart-page-layout #main-cart-footer #checkout::before,
.asl-cart-page-layout #main-cart-footer #checkout::after {
  border-radius: 0 !important;
}
</style>


<style>
/* =========================================================
   CART APP SPACING + SUBTOTAL POSITION
   ========================================================= */

/* Make the app block more compact vertically without changing its layout */
#main-cart-footer .cart__footer > .shopify-app-block,
#main-cart-footer .cart__footer > [data-shopify-editor-block],
#main-cart-footer .cart__blocks > .shopify-app-block,
#main-cart-footer .cart__blocks > [data-shopify-editor-block] {
  margin-top: 0 !important;
  margin-bottom: 6px !important;
  padding-top: 4px !important;
  padding-bottom: 4px !important;
}

/* Remove extra outer whitespace from the first/last element inside the app */
#main-cart-footer .shopify-app-block > :first-child,
#main-cart-footer [data-shopify-editor-block] > :first-child {
  margin-top: 0 !important;
}

#main-cart-footer .shopify-app-block > :last-child,
#main-cart-footer [data-shopify-editor-block] > :last-child {
  margin-bottom: 0 !important;
}

/* Keep subtotal close to the checkout area */
#main-cart-footer .js-contents {
  margin-bottom: 10px !important;
}

#main-cart-footer .js-contents + .asl-checkout-stack {
  margin-top: 0 !important;
}
</style>

<script>
(() => {
  const placeSubtotalBeforeCheckout = () => {
    const footer = document.getElementById('main-cart-footer');
    if (!footer) return;

    const blocks = footer.querySelector('.cart__blocks');
    if (!blocks) return;

    const subtotal = blocks.querySelector('.js-contents');
    const checkoutStack = blocks.querySelector('.asl-checkout-stack');

    if (!subtotal || !checkoutStack) return;

    /* Enforce this exact order:
       ... app / note / gift wrap ...
       subtotal
       checkout buttons
    */
    if (subtotal.nextElementSibling !== checkoutStack) {
      checkoutStack.insertAdjacentElement('beforebegin', subtotal);
    }
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', placeSubtotalBeforeCheckout);
  } else {
    placeSubtotalBeforeCheckout();
  }

  document.addEventListener('shopify:section:load', placeSubtotalBeforeCheckout);
})();
</script>


<style>
/* =========================================================
   TABLET CART LAYOUT FIX — 750px to 989px
   Keep the cart readable and stop the right-side content from
   being squeezed into tiny columns.
   ========================================================= */
@media screen and (min-width: 750px) and (max-width: 989px) {

  /* Main cart becomes one clean vertical column on tablet */
  .asl-cart-page-layout {
    display: block !important;
    width: 100% !important;
    max-width: none !important;
    margin: 0 !important;
    padding: 28px 32px 56px !important;
    box-sizing: border-box !important;
  }

  .asl-cart-page-layout > .shopify-section {
    width: 100% !important;
    max-width: none !important;
    min-width: 0 !important;
    margin: 0 !important;
  }

  /* Give the cart items some breathing room before the summary */
  .asl-cart-page-layout #main-cart-items {
    width: 100% !important;
    max-width: none !important;
    margin-bottom: 32px !important;
  }

  /* Summary/footer uses full tablet width */
  .asl-cart-page-layout #main-cart-footer,
  .asl-cart-page-layout #main-cart-footer > .page-width,
  .asl-cart-page-layout #main-cart-footer .cart__footer {
    position: static !important;
    top: auto !important;

    width: 100% !important;
    max-width: none !important;
    min-width: 0 !important;

    margin: 0 !important;
    padding: 0 !important;
  }

  /* Everything in the summary stacks vertically */
  #main-cart-footer .cart__footer,
  #main-cart-footer .cart__blocks,
  #main-cart-footer .asl-checkout-stack {
    display: flex !important;
    flex-direction: column !important;
    width: 100% !important;
    max-width: none !important;
    min-width: 0 !important;
  }

  #main-cart-footer .cart__blocks {
    gap: 0 !important;
  }

  /* App block: full width, compact */
  #main-cart-footer .cart__footer > .shopify-app-block,
  #main-cart-footer .cart__footer > [data-shopify-editor-block],
  #main-cart-footer .cart__blocks > .shopify-app-block,
  #main-cart-footer .cart__blocks > [data-shopify-editor-block] {
    width: 100% !important;
    max-width: none !important;
    min-width: 0 !important;

    margin: 0 0 12px !important;
    padding: 4px 0 !important;

    box-sizing: border-box !important;
  }

  /* Notes + gift wrap no longer sit as tiny pills beside other content */
  #main-cart-footer .asl-cart-note-accordion,
  #main-cart-footer .asl-cart-giftwrap-trigger-wrap {
    width: 100% !important;
    max-width: none !important;
    min-width: 0 !important;

    margin-left: 0 !important;
    margin-right: 0 !important;
  }

  #main-cart-footer .asl-cart-note-accordion {
    margin-bottom: 10px !important;
  }

  #main-cart-footer .asl-cart-giftwrap-trigger-wrap {
    margin-bottom: 16px !important;
    padding: 0 !important;
    border: 0 !important;
  }

  #main-cart-footer .asl-cart-accordion__summary,
  #main-cart-footer .asl-cart-giftwrap-trigger {
    width: 100% !important;
    max-width: none !important;

    min-height: 52px !important;
    height: auto !important;

    padding: 0 18px !important;
    box-sizing: border-box !important;
  }

  /* Subtotal is a proper full-width row before checkout */
  #main-cart-footer .js-contents {
    width: 100% !important;
    max-width: none !important;
    min-width: 0 !important;

    margin: 8px 0 14px !important;
    padding: 16px 0 0 !important;

    border-top: 1px solid rgba(8, 4, 76, .10) !important;
  }

  #main-cart-footer .totals {
    display: flex !important;
    align-items: baseline !important;
    justify-content: space-between !important;
    gap: 20px !important;

    width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
  }

  #main-cart-footer .totals__total,
  #main-cart-footer .totals__total-value {
    margin: 0 !important;
    font-size: 18px !important;
    line-height: 1.25 !important;
  }

  #main-cart-footer .tax-note {
    display: block !important;
    width: 100% !important;

    margin: 8px 0 16px !important;

    text-align: left !important;
    font-size: 12px !important;
    line-height: 1.45 !important;
  }

  /* Checkout area gets full width */
  #main-cart-footer .asl-checkout-stack,
  #main-cart-footer .cart__ctas,
  #main-cart-footer .cart__dynamic-checkout-buttons,
  #main-cart-footer .additional-checkout-buttons {
    width: 100% !important;
    max-width: none !important;
    min-width: 0 !important;
  }

  #main-cart-footer .asl-checkout-stack {
    row-gap: 6px !important;
  }

  #main-cart-footer #checkout {
    width: 100% !important;
    min-height: 54px !important;

    margin: 0 !important;

    border-radius: 0 !important;
  }

  #main-cart-footer #checkout::before,
  #main-cart-footer #checkout::after {
    border-radius: 0 !important;
  }

  /* Payment icons use the available tablet width and wrap naturally */
  #main-cart-footer .asl-checkout-payment-methods {
    width: 100% !important;
    margin: 6px 0 0 !important;
  }

  #main-cart-footer .asl-checkout-payment-methods__icons {
    display: flex !important;
    flex-wrap: wrap !important;
    justify-content: center !important;
    align-items: center !important;

    width: 100% !important;
    gap: 6px !important;
  }

  #main-cart-footer .asl-checkout-payment-method svg {
    max-width: 44px !important;
    height: 22px !important;
  }

  /* Prevent any child from forcing horizontal overflow */
  #main-cart-footer *,
  .asl-cart-page-layout * {
    min-width: 0;
  }
}
</style>


<style>
/* =========================================================
   TABLET CART — BALANCED 2-COLUMN SUMMARY
   750px–989px
   ========================================================= */
@media screen and (min-width: 750px) and (max-width: 989px) {

  /* Keep the whole cart comfortably wide */
  .asl-cart-page-layout {
    display: block !important;
    width: 100% !important;
    max-width: none !important;
    margin: 0 !important;
    padding: 24px 28px 42px !important;
    box-sizing: border-box !important;
  }

  .asl-cart-page-layout #main-cart-items {
    width: 100% !important;
    max-width: none !important;
    margin: 0 0 20px !important;
  }

  .asl-cart-page-layout #main-cart-footer,
  .asl-cart-page-layout #main-cart-footer > .page-width {
    width: 100% !important;
    max-width: none !important;
    margin: 0 !important;
    padding: 0 !important;
  }

  /*
    Tablet summary:
    LEFT  = BOX NOW / app
    RIGHT = note + gift wrap + subtotal + checkout
  */
  .asl-cart-page-layout #main-cart-footer .cart__footer {
    position: static !important;
    top: auto !important;

    display: grid !important;
    grid-template-columns: minmax(0, 1.15fr) minmax(290px, .85fr) !important;
    column-gap: 28px !important;
    row-gap: 10px !important;
    align-items: start !important;

    width: 100% !important;
    max-width: none !important;
    margin: 0 !important;
    padding: 18px 0 0 !important;

    border-top: 1px solid rgba(8, 4, 76, .10) !important;
  }

  /* App/BOX NOW stays in the left column */
  #main-cart-footer .cart__footer > .shopify-app-block,
  #main-cart-footer .cart__footer > [data-shopify-editor-block] {
    grid-column: 1 !important;

    width: 100% !important;
    max-width: none !important;
    min-width: 0 !important;

    margin: 0 !important;
    padding: 0 !important;
  }

  /* Compact the app's own top/bottom whitespace */
  #main-cart-footer .cart__footer > .shopify-app-block > :first-child,
  #main-cart-footer .cart__footer > [data-shopify-editor-block] > :first-child {
    margin-top: 0 !important;
  }

  #main-cart-footer .cart__footer > .shopify-app-block > :last-child,
  #main-cart-footer .cart__footer > [data-shopify-editor-block] > :last-child {
    margin-bottom: 0 !important;
  }

  /* Right column */
  #main-cart-footer .asl-cart-note-accordion,
  #main-cart-footer .asl-cart-giftwrap-trigger-wrap,
  #main-cart-footer .cart__blocks {
    grid-column: 2 !important;

    width: 100% !important;
    max-width: none !important;
    min-width: 0 !important;
  }

  /* Notes + gift bag: compact full-width controls */
  #main-cart-footer .asl-cart-note-accordion {
    margin: 0 0 8px !important;
  }

  #main-cart-footer .asl-cart-giftwrap-trigger-wrap {
    margin: 0 0 10px !important;
    padding: 0 !important;
    border: 0 !important;
  }

  #main-cart-footer .asl-cart-accordion__summary,
  #main-cart-footer .asl-cart-giftwrap-trigger {
    width: 100% !important;
    max-width: none !important;

    min-height: 48px !important;
    height: 48px !important;

    margin: 0 !important;
    padding: 0 14px !important;

    border-radius: 999px !important;
    box-sizing: border-box !important;

    font-size: 12px !important;
  }

  /* Cart blocks on the right should be one normal vertical stack */
  #main-cart-footer .cart__blocks {
    display: flex !important;
    flex-direction: column !important;
    gap: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
  }

  /* Subtotal immediately before checkout */
  #main-cart-footer .js-contents {
    order: 1 !important;

    width: 100% !important;
    max-width: none !important;

    margin: 2px 0 12px !important;
    padding: 12px 0 0 !important;

    border-top: 1px solid rgba(8, 4, 76, .10) !important;
  }

  #main-cart-footer .totals {
    display: flex !important;
    align-items: baseline !important;
    justify-content: space-between !important;
    gap: 14px !important;

    width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
  }

  #main-cart-footer .totals__total,
  #main-cart-footer .totals__total-value {
    margin: 0 !important;

    font-size: 15px !important;
    line-height: 1.2 !important;
    white-space: nowrap;
  }

  #main-cart-footer .tax-note {
    width: 100% !important;

    margin: 6px 0 10px !important;

    font-size: 10px !important;
    line-height: 1.35 !important;
    text-align: left !important;
  }

  /* Checkout comes directly after subtotal */
  #main-cart-footer .asl-checkout-stack {
    order: 2 !important;

    display: flex !important;
    flex-direction: column !important;
    row-gap: 5px !important;

    width: 100% !important;
    max-width: none !important;

    margin: 0 !important;
    padding: 0 !important;
  }

  #main-cart-footer .cart__ctas,
  #main-cart-footer .cart__dynamic-checkout-buttons,
  #main-cart-footer .additional-checkout-buttons {
    width: 100% !important;
    max-width: none !important;

    margin: 0 !important;
  }

  #main-cart-footer #checkout {
    width: 100% !important;
    min-height: 50px !important;
    height: 50px !important;

    margin: 0 !important;
    padding: 0 14px !important;

    border-radius: 0 !important;

    font-size: 12px !important;
  }

  #main-cart-footer #checkout::before,
  #main-cart-footer #checkout::after {
    border-radius: 0 !important;
  }

  /* Payment icons: readable, compact, no tiny stretched row */
  #main-cart-footer .asl-checkout-payment-methods {
    width: 100% !important;

    margin: 5px 0 0 !important;
    padding: 0 !important;
  }

  #main-cart-footer .asl-checkout-payment-methods__icons {
    display: flex !important;
    flex-wrap: wrap !important;
    justify-content: flex-start !important;
    align-items: center !important;

    width: 100% !important;
    gap: 5px !important;
  }

  #main-cart-footer .asl-checkout-payment-method {
    flex: 0 0 auto !important;
  }

  #main-cart-footer .asl-checkout-payment-method svg {
    width: auto !important;
    max-width: 38px !important;
    height: 20px !important;
  }
}
</style>


<style>
/* =========================================================
   TABLET CART — FINAL CLEANUP
   Fix heading sizes, buttons, spacing and column balance
   ========================================================= */
@media screen and (min-width: 750px) and (max-width: 989px) {

  /* ---------- PAGE / CART HEADER ---------- */
  .asl-cart-page-layout {
    padding: 20px 24px 40px !important;
  }

  #main-cart-items .title-wrapper-with-link,
  #main-cart-items .title-wrapper {
    align-items: center !important;
    margin-bottom: 18px !important;
  }

  #main-cart-items .title,
  #main-cart-items h1,
  #main-cart-items .cart__title {
    margin: 0 !important;
    color: #08044C !important;
    font-size: 28px !important;
    line-height: 1.1 !important;
    font-weight: 400 !important;
    letter-spacing: 0 !important;
  }

  #main-cart-items .underlined-link,
  #main-cart-items .title-wrapper-with-link a {
    font-size: 12px !important;
    line-height: 1.2 !important;
  }

  /* ---------- CART TABLE ---------- */
  #main-cart-items .cart-items {
    width: 100% !important;
  }

  #main-cart-items .cart-items thead th {
    font-size: 8px !important;
    letter-spacing: .12em !important;
    text-transform: uppercase !important;
  }

  #main-cart-items .cart-item {
    align-items: center !important;
  }

  #main-cart-items .cart-item__details,
  #main-cart-items .cart-item__totals {
    min-width: 0 !important;
  }

  #main-cart-items .cart-item__name {
    font-size: 13px !important;
    line-height: 1.25 !important;
  }

  #main-cart-items .product-option,
  #main-cart-items .cart-item__price-wrapper,
  #main-cart-items .price {
    font-size: 11px !important;
    line-height: 1.25 !important;
  }

  /* ---------- SUMMARY GRID ---------- */
  .asl-cart-page-layout #main-cart-footer .cart__footer {
    grid-template-columns: minmax(0, 1.1fr) minmax(320px, .9fr) !important;
    column-gap: 24px !important;
    row-gap: 8px !important;
    padding-top: 16px !important;
  }

  /* ---------- BOX NOW / APP ---------- */
  #main-cart-footer .cart__footer > .shopify-app-block,
  #main-cart-footer .cart__footer > [data-shopify-editor-block] {
    padding: 0 !important;
    margin: 0 !important;
  }

  #main-cart-footer .shopify-app-block h1,
  #main-cart-footer .shopify-app-block h2,
  #main-cart-footer .shopify-app-block h3,
  #main-cart-footer [data-shopify-editor-block] h1,
  #main-cart-footer [data-shopify-editor-block] h2,
  #main-cart-footer [data-shopify-editor-block] h3 {
    margin-top: 0 !important;
    margin-bottom: 10px !important;
    color: #08044C !important;
    font-size: 15px !important;
    line-height: 1.25 !important;
    font-weight: 700 !important;
  }

  #main-cart-footer .shopify-app-block p,
  #main-cart-footer [data-shopify-editor-block] p {
    margin-top: 0 !important;
    margin-bottom: 10px !important;
    font-size: 12px !important;
    line-height: 1.5 !important;
  }

  #main-cart-footer .shopify-app-block button,
  #main-cart-footer .shopify-app-block a[role="button"],
  #main-cart-footer [data-shopify-editor-block] button,
  #main-cart-footer [data-shopify-editor-block] a[role="button"] {
    min-height: 42px !important;
    padding: 0 16px !important;
    font-size: 11px !important;
    line-height: 1.15 !important;
  }

  /* ---------- NOTE + GIFT BUTTONS ---------- */
  #main-cart-footer .asl-cart-note-accordion,
  #main-cart-footer .asl-cart-giftwrap-trigger-wrap {
    margin-bottom: 8px !important;
  }

  #main-cart-footer .asl-cart-accordion__summary,
  #main-cart-footer .asl-cart-giftwrap-trigger {
    display: flex !important;
    align-items: center !important;

    width: 100% !important;
    height: 48px !important;
    min-height: 48px !important;

    padding: 0 14px !important;

    border-radius: 24px !important;

    font-size: 11px !important;
    line-height: 1.2 !important;
    font-weight: 600 !important;
  }

  #main-cart-footer .asl-cart-accordion__summary > span:first-child,
  #main-cart-footer .asl-cart-giftwrap-trigger > span:last-child {
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
  }

  #main-cart-footer .asl-cart-accordion__icon,
  #main-cart-footer .asl-cart-giftwrap-trigger__icon,
  #main-cart-footer .asl-cart-giftwrap-trigger__icon svg {
    width: 16px !important;
    height: 16px !important;
    min-width: 16px !important;
    flex: 0 0 16px !important;
  }

  /* ---------- SUBTOTAL ---------- */
  #main-cart-footer .js-contents {
    margin: 2px 0 10px !important;
    padding-top: 12px !important;
  }

  #main-cart-footer .totals__total,
  #main-cart-footer .totals__total-value {
    font-size: 14px !important;
    line-height: 1.2 !important;
    white-space: nowrap !important;
  }

  #main-cart-footer .tax-note {
    margin: 6px 0 10px !important;
    font-size: 9px !important;
    line-height: 1.4 !important;
  }

  /* ---------- CHECKOUT BUTTONS ---------- */
  #main-cart-footer .asl-checkout-stack {
    row-gap: 6px !important;
  }

  #main-cart-footer #checkout {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;

    width: 100% !important;
    height: 52px !important;
    min-height: 52px !important;

    margin: 0 !important;
    padding: 0 18px !important;

    border: 0 !important;
    border-radius: 0 !important;

    background: #08044C !important;
    color: #fff !important;

    font-size: 13px !important;
    line-height: 1 !important;
    font-weight: 600 !important;
    letter-spacing: 0 !important;

    box-shadow: none !important;
  }

  #main-cart-footer #checkout::before,
  #main-cart-footer #checkout::after {
    display: none !important;
    content: none !important;
    border-radius: 0 !important;
  }

  /* Do not style Shopify payment button internals; only make wrappers fit */
  #main-cart-footer .cart__dynamic-checkout-buttons,
  #main-cart-footer .additional-checkout-buttons {
    width: 100% !important;
    max-width: none !important;
    margin: 0 !important;
    padding: 0 !important;
  }

  /* ---------- PAYMENT ICONS ---------- */
  #main-cart-footer .asl-checkout-payment-methods {
    margin-top: 6px !important;
  }

  #main-cart-footer .asl-checkout-payment-methods__icons {
    justify-content: flex-start !important;
    gap: 5px !important;
  }

  #main-cart-footer .asl-checkout-payment-method svg {
    max-width: 36px !important;
    height: 19px !important;
  }

  /* ---------- RESPONSIVE SAFEGUARDS ---------- */
  #main-cart-footer .cart__footer > *,
  #main-cart-footer .cart__blocks > *,
  #main-cart-items * {
    min-width: 0 !important;
    box-sizing: border-box !important;
  }
}

/* Slightly narrower tablets: stack summary to avoid cramped controls */
@media screen and (min-width: 750px) and (max-width: 840px) {
  .asl-cart-page-layout #main-cart-footer .cart__footer {
    display: flex !important;
    flex-direction: column !important;
    gap: 12px !important;
  }

  #main-cart-footer .cart__footer > .shopify-app-block,
  #main-cart-footer .cart__footer > [data-shopify-editor-block],
  #main-cart-footer .asl-cart-note-accordion,
  #main-cart-footer .asl-cart-giftwrap-trigger-wrap,
  #main-cart-footer .cart__blocks {
    width: 100% !important;
    max-width: none !important;
  }

  #main-cart-footer .asl-cart-accordion__summary,
  #main-cart-footer .asl-cart-giftwrap-trigger {
    font-size: 12px !important;
  }
}
</style>


<style>
/* =========================================================
   PAYMENT ICONS — CENTER ALIGNMENT
   ========================================================= */
#main-cart-footer .asl-checkout-payment-methods {
  width: 100% !important;
  text-align: center !important;
}

#main-cart-footer .asl-checkout-payment-methods__icons,
.asl-cart-page-layout #main-cart-footer .asl-checkout-payment-methods__icons {
  display: flex !important;
  flex-wrap: wrap !important;
  justify-content: center !important;
  align-items: center !important;
  width: 100% !important;
  margin-left: auto !important;
  margin-right: auto !important;
}
</style>


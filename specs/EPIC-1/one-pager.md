# EPIC-1: Notify customers when an order ships

Owner: Product

## Problem
Customers place an order and then hear nothing. They contact support to ask "where is my order?", which is slow for them and costly for us.

## Goal
Tell customers automatically, by email, the moment their order ships, and let them (and support) check an order's shipping status at any time.

## User stories (high level)
- As a warehouse operator, I can mark an order as shipped.
- As a customer, I receive an email when my order ships.
- As a customer or support agent, I can look up whether an order has shipped.

## Product expectations
- Orders: marking an order shipped announces an `order.shipped` event, and `GET /orders/:id/status` reports the current status.
- Notifications: consumes `order.shipped` and sends the customer an email.
- No other services are expected to change.

## Success metric
- 80% fewer "where is my order?" support contacts within 60 days of launch.
- Shipping email sent within 1 minute of an order being marked shipped, for 99% of orders.

## Out of scope
- SMS or push notifications.
- Carrier tracking numbers and delivery-status updates.
- Email templates beyond a plain-text message.
- Customer notification preferences or unsubscribe.

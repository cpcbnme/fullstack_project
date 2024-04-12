interface Order {
    id: number;
    created: string;
    paid: boolean;
    subtotal: string;
    taxes: string;
    discounts: string;
    items: OrderItem[];
}

interface OrderItem {
    name: string;
    price_per_unit: string;
    quantity: number;
}


export type {Order, OrderItem};
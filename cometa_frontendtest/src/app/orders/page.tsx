import { Button } from "@mui/material";
import { Order } from "@/utils/types/orders";
import OrderTableInfo from "@/components/OrderTableInfo";
import CreateOrderModal from "@/components/CreateOrderModal";

export default async function StockPage() {
	try {
		await fetch(`${process.env.API_URL}/beers`);
	} catch (e) {
		return (
			<>
				<p>Unable to fetch data.</p>
			</>
		);
	}

	const orderData: Order[] = await fetch(`${process.env.API_URL}/beers`).then(
		(res) => res.json()
	);
	return (
		<>
			<OrderTableInfo info={orderData} />
			<div className={"mt-12"}>
				<CreateOrderModal />
			</div>
		</>
	);
}

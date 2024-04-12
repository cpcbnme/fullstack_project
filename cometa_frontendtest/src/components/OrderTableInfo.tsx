import {Order} from "@/utils/types/orders";
import {Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow} from "@mui/material";

export default function OrderTableInfo({info}: { info: Order[] }) {
    return (<>
        <TableContainer component={Paper}>
            <Table sx={{minWidth: 650}} aria-label="simple table">
                <TableHead>
                    <TableRow>
                        <TableCell>Description</TableCell>
                        <TableCell align="right">Amount</TableCell>
                        <TableCell align="right">Discounts</TableCell>
                        <TableCell align="right">Taxes</TableCell>
                        <TableCell align="center">Paid</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {info.map((row: Order) => (
                        <TableRow
                            key={row.id}
                            sx={{'&:last-child td, &:last-child th': {border: 0}}}
                        >
                            <TableCell component="th" scope="row">
                                {row.items.map(item => `${item.quantity}x ${item.name}`).join(", ")}
                            </TableCell>
                            <TableCell align="right">{row.subtotal}</TableCell>
                            <TableCell align="right">{row.discounts}</TableCell>
                            <TableCell align="right">{row.taxes}</TableCell>
                            <TableCell align="center">{row.paid ?
                                <span className={"text-green-500"}>Paid</span> :
                                <span className={"text-red-500"}>Not paid</span>
                            }</TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    </>)
}
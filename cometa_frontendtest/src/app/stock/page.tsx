import {Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow} from "@mui/material";

interface RowInfo {
    name: string;
    price: number;
    quantity: number;
}
export default async function StockPage() {
    const stockData = await fetch("http://localhost:8000/beers").then(res => res.json());
    return (
        <>
            <TableContainer component={Paper}>
                <Table sx={{minWidth: 650}} aria-label="simple table">
                    <TableHead>
                        <TableRow>
                            <TableCell>Name (Beer brand)</TableCell>
                            <TableCell align="right">Price</TableCell>
                            <TableCell align="right">Quantity</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {stockData.map((row: RowInfo) => (
                            <TableRow
                                key={row.name}
                                sx={{'&:last-child td, &:last-child th': {border: 0}}}
                            >
                                <TableCell component="th" scope="row">
                                    <span className={"font-bold"}>{row.name}</span>
                                </TableCell>
                                <TableCell align="right">{row.price}</TableCell>
                                <TableCell align="right">{row.quantity}</TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </>)
}
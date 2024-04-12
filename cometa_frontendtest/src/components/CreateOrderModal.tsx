"use client";

import {
    Box,
    Button,
    FormControl,
    Grid,
    InputLabel,
    MenuItem,
    Modal,
    Select,
    SelectChangeEvent,
    TextField
} from "@mui/material";
import {ChangeEvent, useEffect, useState} from "react";
import {StockInfo} from "@/utils/types/stock";

const style = {
    position: 'absolute' as 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 400,
    bgcolor: 'background.paper',
    color: 'white',
    boxShadow: 24,
    pt: 2,
    px: 4,
    pb: 3,
};

export default function CreateOrderModal() {
    const [open, setOpen] = useState(false)
    const [stock, setStock] = useState<Array<StockInfo>>([]);
    const [selectedItem, setSelectedItem] = useState('');
    const [selectedItemQuantity, setSelectedItemQuantity] = useState(0);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch("/api/stocks", {});
                const data = await response.json();
                setStock(data.data);
            } catch (error) {
                console.error("Error fetching data:", error);
            }
        };

        fetchData();
    }, []);

    function getQuantityByName(name: string) {
        return stock.find((item) => item.name == name)?.quantity
    }

    useEffect(() => {

    }, []);

    const handleClose = () => {
        open && setOpen(!open)
    }

    const handleOpen = () => {
        !open && setOpen(!open)
    }

    const handleChange = (event: SelectChangeEvent) => {
        setSelectedItem(event.target.value as string);
    };

    const placeOrder = async () => {
        const res = await fetch('/api/orders', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({items: [{name: selectedItem, quantity: selectedItemQuantity}]})
        })

        console.log(res)
    }

    const handleQuantitySelected = (event: ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        setSelectedItemQuantity(Number(event.target.value));
    };

    return (
        <>
            <Button variant={"contained"} onClick={handleOpen}>New order</Button>
            <Modal
                open={open}
                onClose={handleClose}
                aria-labelledby="parent-modal-title"
                aria-describedby="parent-modal-description"
            >
                <Box sx={{...style, width: 400}}>
                    <h2 id="parent-modal-title" className={"text-2xl font-bold"}>Create new order</h2>
                    <p id="parent-modal-description">
                        Wanna drink more? Ok, just let us know.
                    </p>

                    <Box component="form" sx={{display: 'flex', flexWrap: 'wrap'}}>
                        <FormControl fullWidth sx={{
                            marginTop: 2,
                            minWidth: 130
                        }}>
                            <InputLabel id="select-beer-label">Beer</InputLabel>
                            <Select
                                labelId="select-beer-label"
                                id="demo-simple-select"
                                value={selectedItem}
                                label="Beer"
                                onChange={handleChange}
                            >
                                {stock.map((item) => (
                                    <MenuItem value={item.name}>{item.name}</MenuItem>
                                ))}
                            </Select>
                        </FormControl>

                        {selectedItem && <FormControl fullWidth sx={{
                            marginTop: 2,
                            minWidth: 130
                        }}>
                            <TextField
                                id="select-quantity-label"
                                label="Quantity"
                                defaultValue={0}
                                value={selectedItemQuantity}
                                onChange={handleQuantitySelected}
                                helperText={`How many ${selectedItem} you want?`}
                            />
                            {selectedItem && (<p className={"text-blue-400"}>
                                We currently have {getQuantityByName(selectedItem)} {selectedItem}(s)
                            </p>)}
                        </FormControl>}
                    </Box>

                    <Button variant={"contained"} sx={{
                        marginTop: 2
                    }}
                            onClick={placeOrder}
                    >
                        Place order
                    </Button>
                </Box>

            </Modal>
        </>
    )
}
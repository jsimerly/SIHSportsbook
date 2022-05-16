import React, { Component } from "react";
import {
    Grid,
    List,
    ListItem,
    Button,
    TextField,
    Box
 } from '@mui/material';

export default function BetSlip(props){
    return (
        <div>
            <Box sx={{
                display: 'flex',
                alignItems: 'center',
                flexDirection: 'column',
                p: 1,
                m: 1,
                borderRadius: 1,
                }}
            >
                <Grid container>
                    <Grid item>
                        Bet Slip Title
                    </Grid>
                    <Grid item>
                        <Button>
                            parlay
                        </Button>
                    </Grid>
                </Grid>
                <List>
                    {['Bet 1', 'Bet 2'].map((bet, index) =>
                        <ListItem>
                            {bet}
                        </ListItem>
                    )}
                </List>
                <TextField
                    label="Wager"
                />
                <Button>
                    Place Bet
                </Button>
            </Box>
        </div>
    )
}
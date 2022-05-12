import React, { Component, useState } from "react";
import { render } from "react-dom";
import {
    Box,
    Grid,
    ToggleButton,
    ToggleButtonGroup,
} from '@mui/material'


export default function Playground(props){
    const [bets, setBets] =  useState([])

    const handleBetSelected = (event, newBets) => {
        setBets(newBets);
    }

    function betButton(val) {
        const button = (
            <ToggleButton value={val}>
                {val}
            </ToggleButton>
        )

        return button
    }

    return (
        <div>
            <ToggleButtonGroup
                value={bets}
                onChange={handleBetSelected}
            >       
                {betButton('test1')}
                {betButton('test2')}
                {betButton('test3')}
            </ToggleButtonGroup> 
        </div>
    )
}

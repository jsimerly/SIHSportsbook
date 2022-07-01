import React, { Component, useState, useEffect } from "react";
import {
    Grid,
    List,
    Button,
    Box,
    IconButton,
    Typography
 } from '@mui/material';

 export default function SubmitBetButton(props){
    
    return (
        <Button
            onClick={props.handleButtonClicked}
        >
            Submit
        </Button>
    )
 }
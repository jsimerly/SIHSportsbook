import { Drawer, ListItem } from "@mui/material";
import React, { Component, useEffect } from "react";
import { Box } from "@mui/system";
import { Divider } from "@mui/material";
import { List } from "@mui/material";

import LeagueButton from "../atoms/LeagueButton";
import LeagueHeader from "../molecules/LeagueHeader";
import PlacedBets from "../molecules/PlacedBets";
import ParlayedPlacedBets from "../molecules/ParlayedPlacedBet";

export default function DrawerComp(props){
    console.log(props)
    const drawer = (
        <div>
            <LeagueHeader/>
                {props.leagues?.map((league, index) => {
                    return (
                        <LeagueButton 
                            league={league}
                            setLeague={props.setLeague}
                        />
                    )
                })}
          
            <Divider/>
            <List>
                {props.openBets?.map((bet, index) => {
                    if (bet.parlayed){
                        return <ParlayedPlacedBets bet={bet}/>
                    }
                    return <PlacedBets bet={bet}/>
                })}
            </List>
            <Divider/>
            <List>
                {props.closedBets?.map((bet, index) => 
                    <ListItem>
                        {bet}
                    </ListItem>
                )}
            </List>
        </div>
    )
        
    return (
    <Box>
        {drawer}
    </Box>
    )
}
  
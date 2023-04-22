/*
* This header file contains the raw data for each of the nodes from The Things Network 
*
*/

// board_config.h
#ifndef LORA_h
#define LORA_H

typedef struct {
  const char *devAddr;
  const char *nwkSKey;
  const char *appSKey;
} NodeData;

enum Board {
    BOARD_ONE,
    BOARD_TWO,
    BOARD_THREE,
    BOARD_FOUR,
    BOARD_FIVE
};

const int nodeAmount = 5;

NodeData nodeArray[nodeAmount] = {
  {"260C3A69", "7A1D49B443E1D436C2AB625F29E0FA8F", "3CD950BBEB0A257C81CAF3C169AF7A07"},
  {"260CB382", "95E4D6790F89D220049DDEB5DDE0C366","7093943351DCD51BC32B4D02C33FF3EC"},
  {"260CAD49", "AC37605D4CD0148891D1FC4FCFBFA10B","044254E3B7972891D76941B12ADE640F"},
  {"260C6769", "5EA5712D08A80C720F820006B7EF54CB","F8AC6991FCC906F18A685868FA34CA0D"},
  {"260C373A", "D01699A8F253EE21901AACBA58700F1E","81C91063912EC354DCF5A2DB024F3EDC"},

  // Add the rest of your node data here
};



#endif
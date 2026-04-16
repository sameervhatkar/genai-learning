ticket_type = input("Enter ticket type (Sleeper / AC / General / Luxury): ").lower()

match ticket_type:
    case "sleeper":
        print("Sleeper – No AC, beds available")

    case "ac":
        print("AC – Air conditioned, comfy ride")

    case "general":
        print("General – Cheapest option, no reservation")

    case "luxury":
        print("Luxury – Premium seats with meals")

    case _:
        print("Invalid ticket type entered")
name = input("whats your name ")

match name:
    case "Moki" | "Leakey" | "Job" | "Dama" | "Jersley" | "Tinah" | "Annah" :
        print("You belong to the Daniel's Family")
    case "irene" | "betty" | "Grace" | "Vicky" | "Christopher"| "Mwendwa" | "Faith":
        print("You belong to the Kisonge's Family")
    case _:
        print("which family do you belong?")

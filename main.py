import flet as ft

def main(page: ft.Page):
    page.title = "Space Station Bravo - Crisis Control"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.theme_mode = ft.ThemeMode.DARK

    # State variables
    game_stage = [1]  # 1: Starlight mission, 2: Moonlight fix, 3: Launch emergency
    click_count = [0]

    # UI Header Elements
    title_text = ft.Text("🚨 MISSION CONTROL: CRISIS ACTIVE", size=22, weight=ft.FontWeight.BOLD, color="red_accent")
    subtitle_text = ft.Text("Astronaut Maya: 'Mission Control! Solar glare has blinded our sensors!'", size=14, color="white70")
    
    instruction_text = ft.Text("📋 TASK 1: Type 'starlight' to activate Solar Filter Mode.", size=14, color="yellow", weight=ft.FontWeight.BOLD)

    # Input Field
    user_input = ft.TextField(
        label="Enter Command Code...",
        width=380,
        autofocus=True,
        border_color="cyan"
    )

    # Status Display Card
    output_card = ft.Container(
        content=ft.Text("Status: Waiting for Mission Control response...", size=15, color="white"),
        padding=15,
        border_radius=10,
        bgcolor="blue_grey_900",
        width=380
    )

    # Forward declaration for the button
    action_button = ft.FilledButton(content="Transmit Code")

    # Command Logic
    def handle_submit(e):
        val = user_input.value.strip().lower()

        # TASK 1: Starlight Mode
        if game_stage[0] == 1:
            if val == "starlight":
                game_stage[0] = 2
                page.theme_mode = ft.ThemeMode.LIGHT
                title_text.value = "☀️ SOLAR FILTER ACTIVE"
                title_text.color = "amber_800"
                subtitle_text.value = "Astronaut Maya: 'Sensors cleared! Now cool down the core!'"
                instruction_text.value = "📋 TASK 2: Type 'moonlight' to trigger the lunar shield."
                output_card.bgcolor = "amber_100"
                output_card.content = ft.Text("✨ Solar filters engaged! Core thermal levels critical.", size=15, color="amber_900")
            else:
                output_card.bgcolor = "blue_grey_900"
                output_card.content = ft.Text(f"❌ Invalid Code '{val}'. You must type 'starlight'!", size=15, color="red_accent")

        # TASK 2: Moonlight Fix
        elif game_stage[0] == 2:
            if val == "moonlight":
                game_stage[0] = 3
                page.theme_mode = ft.ThemeMode.DARK
                title_text.value = "⚠️ SYSTEM FAILURE AT STATION"
                title_text.color = "orange_accent"
                subtitle_text.value = "Astronaut Maya: 'The station thrusters failed! You must come up here!'"
                instruction_text.value = "📋 TASK 3: Clear the input box and click the button 3 times to launch!"
                output_card.bgcolor = "blue_grey_900"
                output_card.content = ft.Text("🌙 Lunar shield active! Mission Control shuttle required on-site.", size=15, color="cyan")
            else:
                output_card.bgcolor = "amber_100"
                output_card.content = ft.Text(f"❌ Invalid Code '{val}'. You must type 'moonlight'!", size=15, color="red_900")

        user_input.value = ""
        page.update()

    # Launch Logic (Task 3 & Space Rescue)
    def handle_button_click(e):
        # Stage 1 and 2 require typing text
        if game_stage[0] in [1, 2]:
            if user_input.value.strip() != "":
                handle_submit(e)
            else:
                output_card.content = ft.Text("⚠️ Enter the requested code into the box first!", size=15, color="red_accent")
                page.update()
            return

        # Stage 3: Launch Thrusters sequence
        if game_stage[0] == 3:
            click_count[0] += 1
            if click_count[0] == 1:
                output_card.content = ft.Text("🔴 Thrusters Charging... (Click 2 more times)", size=15, color="orange")
            elif click_count[0] == 2:
                output_card.content = ft.Text("🟡 Launch Warning: 5 Seconds... (Click 1 more time)", size=15, color="yellow")
            elif click_count[0] >= 3:
                game_stage[0] = 4
                user_input.visible = False
                action_button.content = "Mission Accomplished (Reset Game)"
                title_text.value = "🚀 MISSION CONTROL HAS ARRIVED IN SPACE!"
                title_text.color = "green_accent"
                subtitle_text.value = "Astronaut Maya: 'You made it! Station Bravo is saved!'"
                instruction_text.value = "🎉 HERO OF THE MISSION!"
                output_card.bgcolor = "indigo_900"
                output_card.content = ft.Text("✨ You docked with Station Bravo and repaired the station!", size=16, color="white", weight=ft.FontWeight.BOLD)
            page.update()
            return

        # Stage 4: Reset Game back to start
        if game_stage[0] == 4:
            game_stage[0] = 1
            click_count[0] = 0
            user_input.visible = True
            action_button.content = "Transmit Code"
            title_text.value = "🚨 MISSION CONTROL: CRISIS ACTIVE"
            title_text.color = "red_accent"
            subtitle_text.value = "Astronaut Maya: 'Mission Control! Solar glare has blinded our sensors!'"
            instruction_text.value = "📋 TASK 1: Type 'starlight' to activate Solar Filter Mode."
            output_card.bgcolor = "blue_grey_900"
            output_card.content = ft.Text("Status: Waiting for Mission Control response...", size=15, color="white")
            page.update()

    action_button.on_click = handle_button_click

    # Render Layout
    page.add(
        title_text,
        subtitle_text,
        ft.Divider(height=10, color="transparent"),
        instruction_text,
        ft.Divider(height=15, color="transparent"),
        user_input,
        action_button,
        ft.Divider(height=15, color="transparent"),
        output_card
    )

ft.run(main)
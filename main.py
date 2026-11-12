import flet as ft

def main(page: ft.Page):
    page.title = "Input Display App"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.theme_mode = ft.ThemeMode.DARK

    found_starlight = [False]
    found_moonlight = [False]
    found_warp = [False]
    click_count = [0]
    game_completed = [False]

    title_text = ft.Text("Input Display App", size=24, weight=ft.FontWeight.BOLD, color="cyan")
    hint_text = ft.Text("💡 Hint: Secrets must be unlocked in order! (Try special words first, then empty clicks)", size=12, color="white54", italic=True)

    user_input = ft.TextField(
        label="Type something here...", 
        width=320,
        autofocus=True
    )

    output_text = ft.Text(
        value="Your input will appear here!", 
        size=16, 
        weight=ft.FontWeight.BOLD
    )

    secret_status = ft.Text("Secret Mini-Game Progress: 0 / 3 discovered", size=13, color="yellow")
    reset_button = ft.OutlinedButton(content="Reset Secret Game", visible=False)

    def check_completion():
        count = sum([found_starlight[0], found_moonlight[0], found_warp[0]])
        secret_status.value = f"Secret Mini-Game Progress: {count} / 3 discovered"
        
        if count == 3 and not game_completed[0]:
            game_completed[0] = True
            output_text.value = "🎉 CONGRATULATIONS! You unlocked all 3 secrets in perfect sequence!"
            reset_button.visible = True
        elif count < 3:
            reset_button.visible = False

    def handle_submit(e):
        val = user_input.value.strip().lower()

        if val == "starlight":
            if not found_starlight[0]:
                found_starlight[0] = True
                output_text.value = "✨ SECRET PART 1/3 UNLOCKED: 'starlight' activated Solar Mode! Next hint: Try 'moonlight'."
                page.theme_mode = ft.ThemeMode.LIGHT
            else:
                output_text.value = "You already unlocked starlight mode!"

        elif val == "moonlight":
            if not found_starlight[0]:
                output_text.value = "⚠️ Locked! You must unlock 'starlight' before you can use 'moonlight'."
            elif not found_moonlight[0]:
                found_moonlight[0] = True
                output_text.value = "🌙 SECRET PART 2/3 UNLOCKED: 'moonlight' triggered a lunar eclipse! Next hint: Clear the input and click 3 times."
                page.theme_mode = ft.ThemeMode.DARK
            else:
                output_text.value = "You already unlocked moonlight mode!"

        elif val != "":
            output_text.value = f"You typed: {user_input.value}"
        else:
            output_text.value = "Please type something first!"

        user_input.value = ""
        check_completion()
        page.update()

    def handle_button_click(e):
        if user_input.value.strip() != "":
            handle_submit(e)
        else:
            if not found_starlight[0] or not found_moonlight[0]:
                output_text.value = "⚠️ Multi-click warp sequence is locked! Find the text code secrets first."
                page.update()
                return

            if not found_warp[0]:
                click_count[0] += 1
                if click_count[0] == 1:
                    output_text.value = "🔍 System notice: Empty transmission detected... (Click 2 more times)"
                elif click_count[0] == 2:
                    output_text.value = "🔍 System notice: Signal amplifying... (Click 1 more time)"
                elif click_count[0] >= 3:
                    found_warp[0] = True
                    output_text.value = "🚀 SECRET PART 3/3 UNLOCKED: Multi-click warp sequence completed!"
                check_completion()
                page.update()
            else:
                output_text.value = "All secrets unlocked! Type something normally."
                page.update()

    def reset_secrets(e):
        found_starlight[0] = False
        found_moonlight[0] = False
        found_warp[0] = False
        click_count[0] = 0
        game_completed[0] = False
        page.theme_mode = ft.ThemeMode.DARK
        output_text.value = "Secret game reset. Back to normal inputs!"
        secret_status.value = "Secret Mini-Game Progress: 0 / 3 discovered"
        reset_button.visible = False
        page.update()

    reset_button.on_click = reset_secrets

    submit_button = ft.FilledButton(
        content="Display Input", 
        on_click=handle_button_click
    )

    page.add(
        title_text,
        hint_text,
        ft.Divider(height=10, color="transparent"),
        user_input,
        submit_button,
        ft.Divider(height=10, color="transparent"),
        output_text,
        ft.Divider(height=15, color="transparent"),
        secret_status,
        reset_button
    )

ft.run(main)
import flet as ft

# def main(page: ft.Page):
#     def page_resize(e):
#         pw.value = f"{page.width} px"
#         pw.update()

#     page.on_resize = page_resize

#     pw = ft.Text(bottom=50, right=50, style="displaySmall")
#     page.overlay.append(pw)
#     page.add(
#         ft.ResponsiveRow(
#             [
#                 ft.Container(
#                     ft.Text("Column 1"),
#                     padding=5,
#                     bgcolor=ft.colors.YELLOW,
#                     col={"sm": 6, "md": 4, "xl": 2},
#                 ),
#                 ft.Container(
#                     ft.Text("Column 2"),
#                     padding=5,
#                     bgcolor=ft.colors.GREEN,
#                     col={"sm": 6, "md": 4, "xl": 2},
#                 ),
#                 ft.Container(
#                     ft.Text("Column 3"),
#                     padding=5,
#                     bgcolor=ft.colors.BLUE,
#                     col={"sm": 6, "md": 4, "xl": 2},
#                 ),
#                 ft.Container(
#                     ft.Text("Column 4"),
#                     padding=5,
#                     bgcolor=ft.colors.PINK_300,
#                     col={"sm": 6, "md": 4, "xl": 2},
#                 ),
#             ],
#         ),
#         ft.ResponsiveRow(
#             [
#                 ft.TextField(label="TextField 1", col={"md": 4}),
#                 ft.TextField(label="TextField 2", col={"md": 4}),
#                 ft.TextField(label="TextField 3", col={"md": 4}),
#             ],
#             run_spacing={"xs": 10},
#         ),
#     )
#     page_resize(None)

# ft.app(target=main)

# import flet as ft

# def main(page: ft.Page):
#     def button_clicked(e):
#         t.value = f"Dropdown value is:  {dd.value}"
#         page.update()
    
#     t = ft.Text()
#     b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
#     dd = ft.Dropdown(
#         width=100,
#         options=[
#             ft.dropdown.Option(text="daRed",
#                                data=1,
#                                key=1,
#                                                               ),
#             ft.dropdown.Option("Green"),
#             ft.dropdown.Option("Blue"),
#         ],
#     )
#     page.add(dd, b, t)

# ft.app(target=main)

# from estoque import Base, engine, session
# from estoque.models import Produtos

# def deletar_usuario(usuario_id):
#     usuario = session.query(Produtos).filter(Produtos.id == usuario_id).first()
#     print(usuario.nome)
#     if usuario:
#         session.delete(usuario)
#         session.commit()
#         print('deletado')
#     else:
#         print('não encontrado')
    
# deletar_usuario(3)

from flet import *
 
def main(page:Page):
 
	# CREATE FAKE DATA
	data = [
		{
			"name":"john","age":12
		},
		{
			"name":"oppw","age":12
		},
		{
			"name":"jenifer","age":12
		},
		{
			"name":"aaan","age":12
		},
		{
			"name":"buyua","age":12
		},
		{
			"name":"qwmiu","age":12
		},
		{
			"name":"dokoo","age":12
		},
 
	]
 
	resultdata = ListView()
 
 
	resultcon = Container(
		bgcolor="red200",
		padding=10,
		margin=10,
		offset=transform.Offset(-2,0),
		animate_offset = animation.Animation(600,curve="easeIn"),
		content=Column([
			resultdata
 
			])
		)
 
	def searchnow(e):
		mysearch = e.control.value
		result = []
 
		# IF NOT BLANK YOU TEXTFIELD SEARCH THE RUN FUNCTION
		if not mysearch == "":
			resultcon.visible = True
			for item in data:
				if mysearch in item['name']:
					resultcon.offset = transform.Offset(0,0)
					result.append(item)
			page.update()
 
		# IF RESULT THERE DATA THEN PUSH DATA TO WIDGET CONTAINER Resultcon
		if result:
			resultdata.controls.clear()
			print(f"YOu result {result}")
			for x in result:
				resultdata.controls.append(
					Text(f"name : {x['name']} age : {x['age']}",
						size=20,color="white"
 
						)
 
					)
			page.update()
		else:
			resultcon.offset = transform.Offset(-2,0)
			resultdata.controls.clear()
			page.update()
 
	# HIDE RESULT FOR YOU SEARCH DEFAULT
	resultcon.visible = False
 
	txtsearch = TextField(label="Search now",
		on_change=searchnow
		)
 
 
	page.add(
	Column([
	Text("Search Anything",size=30,weight="bold"),
	txtsearch,
	resultcon
	])
		)

app(target=main)

| Slice | HATEOAS recomendado |
|---|---|
|<input type="checkbox"> `list_tasks` | Paginación: `self`, `first`, `previous`, `next`, `last`; cada tarea puede tener `self` |
| <input type="checkbox">`search_tasks` | Los mismos enlaces de paginación, preservando el texto de búsqueda y filtros |
| <input type="checkbox">`get_task` | `self`, `collection`, `update`, `toggle_completion`, `delete` |
| <input type="checkbox">`create_task` | Respuesta con enlace `self` del recurso creado y cabecera HTTP `Location` |
| <input type="checkbox">`update_task` | Recurso actualizado con sus enlaces |
| <input type="checkbox">`toggle_task` | Recurso con el nuevo estado y sus enlaces |
| <input type="checkbox">`delete_task` | `204 No Content`; no requiere cuerpo ni links |
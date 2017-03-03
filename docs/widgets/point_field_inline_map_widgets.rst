Google Map Widget for Django Admin Inlines
==========================================

As you know Django Admin has inline feature and you can add an inline row dynamically. In this case, Django default map widget doesn't initialize widget when created a new inline row.

If you want to use Google Map Widget on admin inlines with no issue, you just need to use ``GooglePointFieldInlineWidget`` class.

**Usage**

.. code-block:: python

    from mapwidgets.widgets import GooglePointFieldInlineWidget

    class DistrictAdminInline(admin.TabularInline):
        model = District
        extra = 3
        formfield_overrides = {
            models.PointField: {"widget": GooglePointFieldInlineWidget}
        }

    class CityAdmin(admin.ModelAdmin):
        inlines = (DistrictAdminInline,)


**Preview**

.. image:: ../_static/images/google-point-field-admin-inline-widget.gif
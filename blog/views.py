from django.shortcuts import render
from datetime import date

# Create your views here.

all_posts = [
    {
        "slug": "post-1",
        "image": "img2.jpg",
        "author": "Daksh",
        "date": date(2023, 1, 24),
        "title": "post 1",
        "excerpt": "Preview Text- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque convallis elementum hendrerit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum malesuada risus vel justo gravida, id ultrices enim varius.",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur faucibus neque quis leo placerat imperdiet. Integer sit amet erat nec sem dapibus vulputate id vitae tortor. Mauris blandit consectetur purus, eu gravida lacus imperdiet sit amet. Phasellus semper ipsum a posuere porttitor. Donec luctus magna ac ante fringilla porta. Sed vitae dapibus leo. Phasellus auctor diam ut eleifend auctor. Fusce malesuada molestie erat et pretium. Nam sit amet quam fringilla lorem aliquet rutrum sed eget mauris.
    
            Aenean mollis suscipit tortor, vitae volutpat lorem. Phasellus id imperdiet quam, ac blandit ipsum. Curabitur lacinia enim vitae nisi elementum malesuada. Nunc aliquet libero lorem, non porttitor risus volutpat non. Phasellus non sapien elit. In at dui augue. Nunc justo felis, vestibulum et rhoncus eu, pretium congue libero. Nulla ac gravida lorem, vitae dignissim odio. Curabitur ut mi a mi vestibulum hendrerit ut vel libero. Mauris ultrices urna eget arcu dignissim, ut sagittis odio euismod. Nullam scelerisque commodo diam, id lacinia mi tempor non.
            
            Nulla dictum tempus urna, vel placerat quam cursus id. Integer vulputate, enim ut lacinia porta, mauris leo imperdiet ipsum, id tincidunt nulla nulla eget nisi. Curabitur a turpis aliquam neque laoreet pretium quis id orci. Nullam pellentesque, nunc vel bibendum venenatis, mi purus eleifend magna, sed sagittis nisl eros lobortis lorem. Aliquam vulputate velit ex, id pharetra lectus dictum a. Vestibulum pulvinar nec leo in euismod. Nullam dapibus nibh ut dui tincidunt, consequat auctor urna elementum. Sed enim ligula, iaculis id venenatis a, tempus ut nisi. Vestibulum sit amet ligula dui. Pellentesque malesuada est eros, eu tristique lorem dapibus vitae. Mauris tincidunt mauris sit amet erat sagittis, in ultrices nisl ullamcorper. Integer ipsum urna, cursus eu blandit eu, faucibus sed mi.
            
            Vivamus aliquet leo elit. Nulla facilisi. Nam rutrum dolor leo, consequat porttitor est fringilla quis. Nunc ullamcorper id nisl nec fringilla. Aenean vitae elementum nunc. Nullam nisi neque, pharetra vitae ornare pretium, vulputate vitae odio. Vivamus in tristique nibh, sit amet fringilla tortor. Vivamus varius nisi a mi interdum fermentum. Nulla rhoncus diam vitae turpis accumsan suscipit. Phasellus purus leo, tincidunt ac dignissim a, feugiat et neque. Nam condimentum sem eget feugiat faucibus. Integer vel tortor at nisi eleifend tempus. Etiam eget velit sollicitudin, volutpat leo aliquet, scelerisque sapien. Pellentesque dolor sapien, facilisis et ante sed, iaculis mollis risus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;
            
            Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Interdum et malesuada fames ac ante ipsum primis in faucibus. Fusce sed viverra turpis, ut tristique odio. Suspendisse potenti. Vivamus elit nibh, faucibus at libero quis, ultrices malesuada augue. Curabitur sodales metus sed est pellentesque, sed sagittis erat vehicula. Vivamus rutrum luctus cursus. Ut malesuada orci non massa fringilla mollis. Etiam fringilla pretium facilisis. Sed commodo vel metus eu feugiat. Nulla vehicula commodo dictum.
        """
    },
    {
        "slug": "post-2",
        "image": "img2.jpg",
        "author": "Daksh",
        "date": date(2023, 1, 25),
        "title": "post 2",
        "excerpt": "Preview Text- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque convallis elementum hendrerit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum malesuada risus vel justo gravida, id ultrices enim varius.",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur faucibus neque quis leo placerat imperdiet. Integer sit amet erat nec sem dapibus vulputate id vitae tortor. Mauris blandit consectetur purus, eu gravida lacus imperdiet sit amet. Phasellus semper ipsum a posuere porttitor. Donec luctus magna ac ante fringilla porta. Sed vitae dapibus leo. Phasellus auctor diam ut eleifend auctor. Fusce malesuada molestie erat et pretium. Nam sit amet quam fringilla lorem aliquet rutrum sed eget mauris.

            Aenean mollis suscipit tortor, vitae volutpat lorem. Phasellus id imperdiet quam, ac blandit ipsum. Curabitur lacinia enim vitae nisi elementum malesuada. Nunc aliquet libero lorem, non porttitor risus volutpat non. Phasellus non sapien elit. In at dui augue. Nunc justo felis, vestibulum et rhoncus eu, pretium congue libero. Nulla ac gravida lorem, vitae dignissim odio. Curabitur ut mi a mi vestibulum hendrerit ut vel libero. Mauris ultrices urna eget arcu dignissim, ut sagittis odio euismod. Nullam scelerisque commodo diam, id lacinia mi tempor non.

            Nulla dictum tempus urna, vel placerat quam cursus id. Integer vulputate, enim ut lacinia porta, mauris leo imperdiet ipsum, id tincidunt nulla nulla eget nisi. Curabitur a turpis aliquam neque laoreet pretium quis id orci. Nullam pellentesque, nunc vel bibendum venenatis, mi purus eleifend magna, sed sagittis nisl eros lobortis lorem. Aliquam vulputate velit ex, id pharetra lectus dictum a. Vestibulum pulvinar nec leo in euismod. Nullam dapibus nibh ut dui tincidunt, consequat auctor urna elementum. Sed enim ligula, iaculis id venenatis a, tempus ut nisi. Vestibulum sit amet ligula dui. Pellentesque malesuada est eros, eu tristique lorem dapibus vitae. Mauris tincidunt mauris sit amet erat sagittis, in ultrices nisl ullamcorper. Integer ipsum urna, cursus eu blandit eu, faucibus sed mi.

            Vivamus aliquet leo elit. Nulla facilisi. Nam rutrum dolor leo, consequat porttitor est fringilla quis. Nunc ullamcorper id nisl nec fringilla. Aenean vitae elementum nunc. Nullam nisi neque, pharetra vitae ornare pretium, vulputate vitae odio. Vivamus in tristique nibh, sit amet fringilla tortor. Vivamus varius nisi a mi interdum fermentum. Nulla rhoncus diam vitae turpis accumsan suscipit. Phasellus purus leo, tincidunt ac dignissim a, feugiat et neque. Nam condimentum sem eget feugiat faucibus. Integer vel tortor at nisi eleifend tempus. Etiam eget velit sollicitudin, volutpat leo aliquet, scelerisque sapien. Pellentesque dolor sapien, facilisis et ante sed, iaculis mollis risus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;

            Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Interdum et malesuada fames ac ante ipsum primis in faucibus. Fusce sed viverra turpis, ut tristique odio. Suspendisse potenti. Vivamus elit nibh, faucibus at libero quis, ultrices malesuada augue. Curabitur sodales metus sed est pellentesque, sed sagittis erat vehicula. Vivamus rutrum luctus cursus. Ut malesuada orci non massa fringilla mollis. Etiam fringilla pretium facilisis. Sed commodo vel metus eu feugiat. Nulla vehicula commodo dictum.
        """
    },
    {
        "slug": "post-3",
        "image": "img3.png",
        "author": "Daksh",
        "date": date(2023, 1, 26),
        "title": "post 3",
        "excerpt": "Preview Text- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque convallis elementum hendrerit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum malesuada risus vel justo gravida, id ultrices enim varius.",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur faucibus neque quis leo placerat imperdiet. Integer sit amet erat nec sem dapibus vulputate id vitae tortor. Mauris blandit consectetur purus, eu gravida lacus imperdiet sit amet. Phasellus semper ipsum a posuere porttitor. Donec luctus magna ac ante fringilla porta. Sed vitae dapibus leo. Phasellus auctor diam ut eleifend auctor. Fusce malesuada molestie erat et pretium. Nam sit amet quam fringilla lorem aliquet rutrum sed eget mauris.

            Aenean mollis suscipit tortor, vitae volutpat lorem. Phasellus id imperdiet quam, ac blandit ipsum. Curabitur lacinia enim vitae nisi elementum malesuada. Nunc aliquet libero lorem, non porttitor risus volutpat non. Phasellus non sapien elit. In at dui augue. Nunc justo felis, vestibulum et rhoncus eu, pretium congue libero. Nulla ac gravida lorem, vitae dignissim odio. Curabitur ut mi a mi vestibulum hendrerit ut vel libero. Mauris ultrices urna eget arcu dignissim, ut sagittis odio euismod. Nullam scelerisque commodo diam, id lacinia mi tempor non.

            Nulla dictum tempus urna, vel placerat quam cursus id. Integer vulputate, enim ut lacinia porta, mauris leo imperdiet ipsum, id tincidunt nulla nulla eget nisi. Curabitur a turpis aliquam neque laoreet pretium quis id orci. Nullam pellentesque, nunc vel bibendum venenatis, mi purus eleifend magna, sed sagittis nisl eros lobortis lorem. Aliquam vulputate velit ex, id pharetra lectus dictum a. Vestibulum pulvinar nec leo in euismod. Nullam dapibus nibh ut dui tincidunt, consequat auctor urna elementum. Sed enim ligula, iaculis id venenatis a, tempus ut nisi. Vestibulum sit amet ligula dui. Pellentesque malesuada est eros, eu tristique lorem dapibus vitae. Mauris tincidunt mauris sit amet erat sagittis, in ultrices nisl ullamcorper. Integer ipsum urna, cursus eu blandit eu, faucibus sed mi.

            Vivamus aliquet leo elit. Nulla facilisi. Nam rutrum dolor leo, consequat porttitor est fringilla quis. Nunc ullamcorper id nisl nec fringilla. Aenean vitae elementum nunc. Nullam nisi neque, pharetra vitae ornare pretium, vulputate vitae odio. Vivamus in tristique nibh, sit amet fringilla tortor. Vivamus varius nisi a mi interdum fermentum. Nulla rhoncus diam vitae turpis accumsan suscipit. Phasellus purus leo, tincidunt ac dignissim a, feugiat et neque. Nam condimentum sem eget feugiat faucibus. Integer vel tortor at nisi eleifend tempus. Etiam eget velit sollicitudin, volutpat leo aliquet, scelerisque sapien. Pellentesque dolor sapien, facilisis et ante sed, iaculis mollis risus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;

            Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Interdum et malesuada fames ac ante ipsum primis in faucibus. Fusce sed viverra turpis, ut tristique odio. Suspendisse potenti. Vivamus elit nibh, faucibus at libero quis, ultrices malesuada augue. Curabitur sodales metus sed est pellentesque, sed sagittis erat vehicula. Vivamus rutrum luctus cursus. Ut malesuada orci non massa fringilla mollis. Etiam fringilla pretium facilisis. Sed commodo vel metus eu feugiat. Nulla vehicula commodo dictum.
        """
    },
    {
        "slug": "post-4",
        "image": "img4.jpg",
        "author": "Daksh",
        "date": date(2023, 1, 27),
        "title": "post 4",
        "excerpt": "Preview Text- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque convallis elementum hendrerit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum malesuada risus vel justo gravida, id ultrices enim varius.",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur faucibus neque quis leo placerat imperdiet. Integer sit amet erat nec sem dapibus vulputate id vitae tortor. Mauris blandit consectetur purus, eu gravida lacus imperdiet sit amet. Phasellus semper ipsum a posuere porttitor. Donec luctus magna ac ante fringilla porta. Sed vitae dapibus leo. Phasellus auctor diam ut eleifend auctor. Fusce malesuada molestie erat et pretium. Nam sit amet quam fringilla lorem aliquet rutrum sed eget mauris.

            Aenean mollis suscipit tortor, vitae volutpat lorem. Phasellus id imperdiet quam, ac blandit ipsum. Curabitur lacinia enim vitae nisi elementum malesuada. Nunc aliquet libero lorem, non porttitor risus volutpat non. Phasellus non sapien elit. In at dui augue. Nunc justo felis, vestibulum et rhoncus eu, pretium congue libero. Nulla ac gravida lorem, vitae dignissim odio. Curabitur ut mi a mi vestibulum hendrerit ut vel libero. Mauris ultrices urna eget arcu dignissim, ut sagittis odio euismod. Nullam scelerisque commodo diam, id lacinia mi tempor non.

            Nulla dictum tempus urna, vel placerat quam cursus id. Integer vulputate, enim ut lacinia porta, mauris leo imperdiet ipsum, id tincidunt nulla nulla eget nisi. Curabitur a turpis aliquam neque laoreet pretium quis id orci. Nullam pellentesque, nunc vel bibendum venenatis, mi purus eleifend magna, sed sagittis nisl eros lobortis lorem. Aliquam vulputate velit ex, id pharetra lectus dictum a. Vestibulum pulvinar nec leo in euismod. Nullam dapibus nibh ut dui tincidunt, consequat auctor urna elementum. Sed enim ligula, iaculis id venenatis a, tempus ut nisi. Vestibulum sit amet ligula dui. Pellentesque malesuada est eros, eu tristique lorem dapibus vitae. Mauris tincidunt mauris sit amet erat sagittis, in ultrices nisl ullamcorper. Integer ipsum urna, cursus eu blandit eu, faucibus sed mi.

            Vivamus aliquet leo elit. Nulla facilisi. Nam rutrum dolor leo, consequat porttitor est fringilla quis. Nunc ullamcorper id nisl nec fringilla. Aenean vitae elementum nunc. Nullam nisi neque, pharetra vitae ornare pretium, vulputate vitae odio. Vivamus in tristique nibh, sit amet fringilla tortor. Vivamus varius nisi a mi interdum fermentum. Nulla rhoncus diam vitae turpis accumsan suscipit. Phasellus purus leo, tincidunt ac dignissim a, feugiat et neque. Nam condimentum sem eget feugiat faucibus. Integer vel tortor at nisi eleifend tempus. Etiam eget velit sollicitudin, volutpat leo aliquet, scelerisque sapien. Pellentesque dolor sapien, facilisis et ante sed, iaculis mollis risus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;

            Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Interdum et malesuada fames ac ante ipsum primis in faucibus. Fusce sed viverra turpis, ut tristique odio. Suspendisse potenti. Vivamus elit nibh, faucibus at libero quis, ultrices malesuada augue. Curabitur sodales metus sed est pellentesque, sed sagittis erat vehicula. Vivamus rutrum luctus cursus. Ut malesuada orci non massa fringilla mollis. Etiam fringilla pretium facilisis. Sed commodo vel metus eu feugiat. Nulla vehicula commodo dictum.
        """
    }

]


def get_date(post):
    return post.get('date')


def landing_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    if len(sorted_posts) >= 3:
        latest_posts = sorted_posts[-3:]
    else:
        latest_posts = sorted_posts

    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts,
    })


def load_post(request, slug):
    selected_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/load-post.html", {
        "post": selected_post,
    })

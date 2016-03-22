using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(Item_58.Startup))]
namespace Item_58
{
    public partial class Startup {
        public void Configuration(IAppBuilder app) {
            ConfigureAuth(app);
        }
    }
}
